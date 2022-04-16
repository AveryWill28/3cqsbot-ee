# Summary
The 3cqsbot can be used to start and stop [3commas](https://3commas.io) dca bots with the help of the 3cqs signals. You can subscribe to the [telegram channel](https://t.me/The3CQSBot) to receive these signals. If you have any questions regarding the signals, please contact the developer [directly](https://www.3cqs.com/contact/).

# Disclaimer
**The 3cqsbot is meant to be used for educational purposes only. Use with real funds at your own risk**

# Prerequisites/Installation

## 3CQS Signals Bot

Join the telegram channel [telegram channel](https://t.me/The3CQSBot) according to the official Telegram [documentation](https://core.telegram.org/api/obtaining_api_id)

Wait for the signals. Actually the signals are in a beta phase and you have to be chosen to get them. Be patient if they not arrive after joining

## Telegram API
In the meantime create your [telegram api account](https://my.telegram.org/apps) and insert them into `api_id` and `api_hash` fields in the *'telegram'* section of the `config.ini`

## 3Commas API
Create a [3commas api account](https://3commas.io/api_access_tokens) too and insert the values in the `key` and `secret` fields in the *'commas'* section of the `config.ini`

**Permissions needed:** BotsRead, BotsWrite, AccountsRead

## Operating Systems
- MacOS
- Linux
    - Ubuntu
- Windows
    - untested (please let me know if it works)
- Docker

## Installation
### Python
Please install at least version 3.7 on your system

### Python modules
```
pip3 install -r requirements.txt
```

# Configuration (config.ini)
Copy the `*.example*` from the examples directory to `config.ini` in the root folder and change your settings regarding the available settings below. The value type doesn't matter, because Pythons configparser is taking care of the types. So you don't need '' or "" around the values.

## General
Name | Type | Mandatory | Values(default) | Description
------------ | ------------ | ------------ | ------------ | ------------
debug | boolean | NO | (false) true   | Set logging to debug
log_to_file | boolean | NO | (false) true  | Log to file instead of console
log_file_path | string | NO | (3cqsbot.log) | Location of the log file
log_file_size | integer | NO | (200000) | Log file size
log_file_count | integer | NO | (5) | How many logfiles will be archived, before deleted

## Telegram
Name | Type | Mandatory | Values(default) | Description
------------ | ------------ | ------------ | ------------ | ------------
api_id | string | YES |   | Telegram API ID
api_hash | string | YES |   | Telegram API Hash
sessionfile | string | NO | (tgsession) | Telegram sessionfile location

**!!! ATTENTION - Do not share your sessionfile with other 3cqsbot instances - this will lead to problems and misfunctional bots. For each instance you have to create a new sessionfile !!!**

## 3Commas
Name | Type | Mandatory | Values(default) | Description
------------ | ------------ | ------------ | ------------ | ------------
chatroom | string |NO | (3C Quick Stats) | Name of the chatroom - on Windows please use the ID 5011413076
key | string | YES |    | 3Commas API Key
secret | string | YES | | 3Commas API Secret
timeout | integer | NO | (3) | Timeout waiting for a 3Commas api response
retries | integer | NO | (5) | Number of retries after a 3Commas api call was not successful
delay_between_retries | number | NO | (2.0) | Waiting time factor between unsuccessful retries
system_bot_value | integer | NO | (300) | Number of actual bots running on your account. This is important, so that the script can see all running bots and does not start duplicates!

## DCABot configuration

Name | Type | Mandatory | Values(default) | Description
------------ | ------------ | ------------ | ------------ | ------------
prefix | string | YES | (3CQSBOT)  | The name prefix of the created bot
subprefix | string | YES | (MULTI) | Subprefix of the bot (Best would be SINGLE or MULTI)
suffix | string | YES | (TA_SAFE) | Suffix in the bot name - could be the used bot configuration
tp | number | YES | (1.5)  | Take profit in percent
bo | number | YES | (11)   | Base order volume
so | number | YES | (11) | Safety order volume
os | number | YES | (1.05) | Safety order volume scale
ss | number | YES | (1) | Safety order step scale
sos | number | YES | (2.4) | Price deviation to open safety orders
mad | integer | YES | (3) | Max active deals for a bot
max | integer | YES | (1) | Max active safety trades count
mstc | integer | YES | (25) | Max safety trades count
sdsp | integer | NO | (1) | Simultaneous deals per same pair (only Multibot)
single | boolean | YES | (false) true | Type of Bot creation (True for Single DCA Bots)
single_count | integer | YES | (3) | Maximum single bots - only have to configured for singlebots
btc_min_vol | number | NO | (100) | Minimum 24h volume trading calculated in BTC
cooldown | number | NO | (30) | Number of seconds to wait until starting another deal
deals_count | integer | NO | (1) | Bot will be disabled after completing this number of deals

Configure the 'dcabot' section in the `config.ini` according to your favourite bot configuration. 

If you don't have any, please take a look at [this site](https://www.buymeacoffee.com/Ribsy/posts) for published settings.

Default configuration is based on Trade Alts Safer settings: https://discord.gg/tradealts

### Note about single/multibot deal/bots settings
#### Singlebot configuration
**single_count** = how many singlebots can run overall

**mad** = how many deals can run on a singlebot pair

**Examples:** 

`single_count=1`, `mad=1` - Only one singlebot is started, and only one deal is started

`single_count=3`, `mad=1` - Three singlebots are started, and only one deal per singlebot is started

`single_count=3`, `mad=2` - Three singlebots are started, and two deals are started per singlebot

#### Multibot configuration
**mad** = how many deals per composite bot can run

**Example:** 

`mad=20` - 20 deals with different pairs can run at the same time


## Trading mode

Name | Type | Mandatory | Values(default) | Description
------------ | ------------ | ------------ | ------------ | ------------
market | string | YES | (USDT)  | Trading market (Example: BUSD, USDT, USDC)
trade_mode | string | YES | (paper) real   | Real or Paper trading mode
account_name | string | YES | (Paper trading 123456)  | Account name for trading. Can be found unter "My Exchanges". 
deal_mode | string | NO | ([{"options": {"time": "3m", "points": "100", "time_period": "7", "trigger_condition": "less"}, "strategy": "rsi"}]) signal | Method how the script is creating new deals in  multipair bot
limit_initial_pairs | boolean |NO | (false) | Limit initial pairs to the max number of deals (MAD) - bot chooses the top pairs
btc_pulse | boolean | NO | (false), true | Activates or deactivates the bots according to Bitcoins behaviour. If Bitcoin is going down, the bot will be disabled
delete_single_bots | boolean | NO | (false), true | If set to true, bots without an active deal will be deleted in single bot configuration
singlebot_update | boolean | NO | (true), false | If set to true, singlebots settings will be updated when enabled again (new settings only work after restart of the script)
trailing | boolean | NO | (false), true | Trailing profit enabled
trailing_deviation | number | NO | (0.2) | Deviation of trailing profit
trade_future | boolean | NO | (false), true | Enable futures trading
leverage_type | string | NO | (cross), custom, not_specified, isolated | Different leverage types for futures trading from 3commas
leverage_value | integer | NO | (2) | Leverage value for futures trading
stop_loss_percent | integer | NO | (1) | Stop loss value in percent for futures trading
stop_loss_type | string | NO | (stop_loss_and_disable_bot), stop_loss | Stop Loss type for futures trading
stop_loss_timeout_enabled | boolean | NO | (false), true | Enable stop loss timeout for futures trading
stop_loss_timeout_seconds | integer | NO | (5) | Time interval for stop loss in seconds for futures trading

### Deal Mode explanation

**single=true deal_mode=signal**

A single bot for a specific pair (the signal) will be created when the signal fits your configured filters and when the signal is a "START" signal. The deal will be start immediately. The bot will be disabled on a stop signal for this specific pair. If `delete_single_bots`is set to true, the script tries do delete the bot. This only works, when no deal is running.

**single=true deal_mode="self asigned strategy"**

Everything is the same as with the other single mode, but the deals are started dependent on your configured `deal_mode` strategy.

**single=false deal_mode=signal**

A multi bot will be created with the top 30 Symrank list (initical call to /symrank). A new deal will be started when a new signal is coming in. 

If it is a STOP/START signal which is not from an existing pair a random pair from the initial top 30 Symrank list is used for a new deal. 

If it is a START signal from an existing pair or a freshly added pair, exactly that pair is used for a new deal.

Pairs will be deleted from the list during a STOP signal and added with a START signal, if it fits the filters.

**single=false deal_mode="self asigned strategy"**

Everything is the same as with the other multi mode, but the deals are started dependent on your configured `deal_mode` strategy.

## Filter

Name | Type | Mandatory | Values(default) | Description
------------ | ------------ | ------------ | ------------ | ------------
symrank_signal | string | YES | (triple100), top30, xvol, hvol, all | Decide which signal the bot should parse.
symrank_limit_min | integer | NO | (1) | Bots will be created when the symrank value is over this limit
symrank_limit_max | integer | NO | (100) | Bots will be created when the symrank value is under this limit
volatility_limit_min | number | NO | (0.1) | Bots will be created when the volatility value is over this limit
volatility_limit_max | number | NO | (100) | Bots will be created when the volatility value is under this limit
price_action_limit_min | number | NO | (0.1) | Bots will be created when the price_action value is over this limit
price_action_limit_max | number | NO | (100) | Bots will be created when the price_action value is under this limit
topcoin_limit | integer | NO | (3500) | Token pair has to be in the configured topcoin limit to be traded by the bot
topcoin_volume | integer | NO | (0) | Volume check against Coingecko (btc_min_vol means volume check directly in 3commas - not before like this setting). Only pairs with the given volume are traded. Default is 0 and means volume check is disabled
topcoin_exchange | string | NO | (binance), gdax | Name of the exchange to check the volume. Because every exchange has another id, please contact me for your exchange and I will update this list here for configuration
deal_mode | string | NO | ([{"options": {"time": "3m", "points": "100"}, "strategy": "rsi"}]) signal | Deal strategy how the script is creating new deals in multipair bot - for more see the "Deal Modes" section
limit_initial_pairs | boolean |NO | (false), true | Limit initial pairs to the max number of deals (MAD) - bot chooses the top pairs
random_pair | boolean | NO | (false), true | If true then random pairs from the symrank list will be used for new deals in multibot
btc_pulse | boolean | NO | (false), true | Activates or deactivates the bots according to Bitcoins behaviour. If Bitcoin is going down, the bot will be disabled
ext_botswitch | boolean | NO | (false), true | If enabled the automatic multibot enablement will be disabled and only triggered by external events - you must disable BTC Pulse if you enable this switch !!!
token_denylist | array |YES | ([BUSD_USDT, USDC_USDT, USDT_USDT, USDT_USDP]) | Denylist of pairs which not be used by the bot for new deals

### Signals
The new version of 3cqs signals is now separated into three main versions. To decide which version fit your needs, please take a look at the indicators beneath. The description can be found on Discord too: https://discord.com/channels/720875074806349874/835100061583015947/958724423513419876

#### triple100
SIGNAL NAME: SymRank Top 100 Triple Tracker
BOT_START: SymRank <= 100
Volatility Score >= 3, 
Price Action Score >= 2

#### top30
SIGNAL NAME: SymRank Top 30
BOT_START: SymRank <= 30

#### xvol
SIGNAL NAME: X-treme Volatility
BOT_START: Volatility Score >= 10

#### hvol
SIGNAL NAME: Hyper Volatility
BOT_START: Volatility Score >= 6

#### all
Pass through all signals

### BTC Pulse
BTCPulse is a simple strategy which monitors BTC Price Action to start new deals or just put the bot to sleep ( no new deals but active deals keep running) based on:-
If BTC is in upswing new deals are started 
If BTC is dumping no new deals are started

BTCPulse hence is determined using the 2 factors :-
% price change of BTC in the last 15 minutes or
Fast and Slow moving EMAs crossses

Please test this strategy on paper before putting real money on it.
TBMoonWalker or IamtheOnewhoKnocks take no responsibility for losses occurred due to the script/strategy

**Again, please use 3cqsbot only on paper trading. Usage with real funds is at your own risk**


### Deal Modes
This section is all about the deal start signals. Tested are the following modes:

- `signal` --> starting the bot after a 3CQS signal
- `[{"options": {"time": "3m", "points": "100"}, "strategy": "rsi"}]` --> start the bot when the RSI-7 value is under 100 in the 3 minute view

More modes are possible, but not tested. You can minimize the value of the RSI-7 entry point for example. A whole list of deal signals can be found with the api call `GET /ver1/bots/strategy_list`. Details can be found under: https://github.com/3commas-io/3commas-official-api-docs/blob/master/bots_api.md

# Run
If you get signals, you can run the script with the command: 

```
python3 3cqsbot.py
```
When running for the first time, you will be asked for your Telegram phonenumber and you will get a code you have to insert!

## You don't get the code
Some users had to put spaces in the phone number. It seems the number has to be the same format as in Telegram. For example type in your telephone number as `+XXX XXX XXX XXX` to receive the code.

# Docker
## Create the docker image
```
docker build -t "your repo name"/3cqsbot:"version number"
```
## Create a persistent volume for your Telegram session file
```
docker volume create session
```

## Create your .env file
Copy one of the `.env.*.example` files from the example directory to `.env` in the root directory and change the settings. The same settings as in the config.ini can be used

## Run your container
```
docker run --name 3cqsbot --volume session:/App/session --env-file .env -d "your repo name"/3cqsbot:"version number"
```

## Logfile monitoring
```
docker logs --follow 3cqsbot
```
# PythonAnywhere
If you want to run 3cqsbot 24h/7d without running your home computer all the time and you do not have a Rasperry Pi, 
then PythonAnywhere might be a cheap option for you to run the script.

## Create account
If you live in the EU go to https://eu.pythonanywhere.com otherwise https://www.pythonanywhere.com.
The 'Hacker account' plan for 5€/5$ is sufficient enough to run 3cqsbot

## Preparing PythonAnywhere to run 3CQSBot
Click on `Dashboard`. Under menue "New console" Click on `$ Bash` to open a Bash console in your home directory.
Clone the actual version of 3cqsbot from Github and install the requirements for the bot by following commands
```
git clone https://github.com/TBMoonwalker/3cqsbot.git 3cqsbot
cd 3cqsbot
pip3 install -r requirements.txt
cp config.ini.example config.ini
```
When you want to use multiple 3cqsbots simultanously you have to clone 3cqsbot to different directories 
```
git clone https://github.com/TBMoonwalker/3cqsbot.git 3cqsbot_TAsafe
git clone https://github.com/TBMoonwalker/3cqsbot.git 3cqsbot_Urmav6
git clone https://github.com/TBMoonwalker/3cqsbot.git 3cqsbot_Mars
```
## Edit config.ini settings
Edit the config.ini with the integrated editor of PythonAnywhere in the `Files` menue. Paste the necessary keys of 3commas and Telegram and 
configure your DCA settings. Once done you can copy your config.ini to other directories of 3cqsbot and adapt the DCA settings.

## Scheduled tasks
Because the consoles of PythonAnywhere are frequently restarted due to maintenance you have to use scheduled task to ensure continuous work of your 3cqsbot.
Before running 3cqsbot as scheduled task, make sure that you run the script once on the console to establish the Telegram security session. 
Enter your phone number (international format, e.g. +49xxx or 0049xxx) of your Telegram account and enter the code you receive from Telegram. 
Check if 3cqsbot is running without any problems under the console. 
Do not copy the tgsession file to other directories of 3cqsbots, because it is an individual security file and you will invalidate the established Telegram session
when used with another version of 3cqsbot.

Click on `Tasks` menue. If you have only one python script running you can use the Always-on task (only one Always-on task allowed on the "Hacker account" plan).
In case of using more scripts, e.g. for testing DCA settings, you have to use scheduled tasks on an hourly basis. Select "Hourly" and paste
```
cd ~/3cqsbot && python 3cqsbot.py 
```
If you encounter problems with this command then try this where YOUR_USERNAME has to be replaced by your chosen username on PythonAnywhere.
```
cd /home/YOUR_USERNAME/3cqsbot && python 3cqsbot.py
```
When using multiple 3cqsbots with different settings you have to add each 3cqsbot directory as seperate hourly task. 
Rename 3cqsbot.py according to your DCA setting configuration in the `Files` menue to identify the task running in the process list.

1. Hourly Task: 10min ```cd ~/3cqsbot_TAsafe && python 3cqsbot_TAsafe.py```
2. Hourly Task: 11min ```cd ~/3cqsbot_Urmav6 && python 3cqsbot_Urmav6.py```
3. Hourly Task: 12min ```cd ~/3cqsbot_Urmav6 && python 3cqsbot_Mars.py```

In case you have to kill a process you can know easily identify your task to kill after fetching the process list under `Running tasks`
Check the log files in the scheduled task under `Actions` for errors.

## Updating 3cqsbot
If you want to update 3cqsbot to the newest version open the Bash console. Change to your desired 3cqsbot directory with following commands
```
cd 3cqsbot
git pull
pip3 install -r requirements.txt
```
Check the config.ini.example for new config options. Make sure to update your existent config.ini for the new options with the integrated 
PythonAnywhere editor (Files menue).

# Debugging
The script can be started with 

```
python3 3cqsbot.py -l debug
```

do show debug logging

# Bug reports
Please submit bugs or problems through the Github [issues page](https://github.com/TBMoonwalker/3cqsbot/issues).

# Donation
If you like to support this project, you can donate to the following wallet:

- USDT or BUSD (BEP20 - Binance Smart Chain): 0xB3C6DD82a203E3b6f399187DB265AdC664E2beF9
