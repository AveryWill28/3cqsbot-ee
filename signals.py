import yfinance as yf
import numpy as np
import asyncio
import math
import re
import babel.numbers

from pycoingecko import CoinGeckoAPI
from tenacity import retry, wait_fixed
from functools import lru_cache, wraps
from time import monotonic_ns


class Signals:
    def __init__(self, logging):
        self.logging = logging

    # Credits goes to @IamtheOnewhoKnocks from
    # https://discord.gg/tradealts
    def ema(self, data, period, smoothing=2):
        # Calculate EMA without dependency for TA-Lib
        ema = [sum(data[:period]) / period]

        for price in data[period:]:
            ema.append(
                (price * (smoothing / (1 + period)))
                + ema[-1] * (1 - (smoothing / (1 + period)))
            )

        for i in range(period - 1):
            ema.insert(0, np.nan)

        return ema

    # Credits goes to @IamtheOnewhoKnocks from
    # https://discord.gg/tradealts
    @retry(wait=wait_fixed(2))
    def btctechnical(self, symbol):
        btcusdt = yf.download(
            tickers=symbol, period="6h", interval="5m", progress=False
        )
        if len(btcusdt) > 0:
            btcusdt = btcusdt.iloc[:, :5]
            btcusdt.columns = ["Time", "Open", "High", "Low", "Close"]
            btcusdt = btcusdt.astype(float)
            btcusdt["EMA9"] = self.ema(btcusdt["Close"], 9)
            btcusdt["EMA50"] = self.ema(btcusdt["Close"], 50)
            btcusdt["per_5mins"] = (np.log(btcusdt["Close"].pct_change() + 1)) * 100
            btcusdt["percentchange_15mins"] = (
                np.log(btcusdt["Close"].pct_change(3) + 1)
            ) * 100
        else:
            raise IOError("Downloading YFinance chart broken, retry....")

        return btcusdt

    # Credits goes to @IamtheOnewhoKnocks from
    # https://discord.gg/tradealts
    async def getbtcbool(self, asyncState):

        self.logging.info("Starting btc-pulse")

        while True:
            btcusdt = self.btctechnical("BTC-USD")
            # if EMA 50 > EMA9 or <-1% drop then the sleep mode is activated
            # else bool is false and while loop is broken
            if (
                btcusdt.percentchange_15mins[-1] < -1
                or btcusdt.EMA50[-1] > btcusdt.EMA9[-1]
            ):
                self.logging.info("btc-pulse signaling downtrend")

                # after 5mins getting the latest BTC data to see if it has had a sharp rise in previous 5 mins
                await asyncio.sleep(300)
                btcusdt = self.btctechnical("BTC-USD")

                # this is the golden cross check fast moving EMA
                # cuts slow moving EMA from bottom, if that is true then bool=false and break while loop
                if (
                    btcusdt.EMA9[-1] > btcusdt.EMA50[-1]
                    and btcusdt.EMA50[-2] > btcusdt.EMA9[-2]
                ):
                    self.logging.info("btc-pulse signaling uptrend")
                    asyncState.btcbool = False
                else:
                    self.logging.info("btc-pulse signaling downtrend")
                    asyncState.btcbool = True

            else:
                self.logging.info("btc-pulse signaling uptrend")
                asyncState.btcbool = False

            self.logging.info("Next btc-pulse check in 5m")
            await asyncio.sleep(300)
