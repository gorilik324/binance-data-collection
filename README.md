# Binance Data Collection

Collects daily candlestick data and order book data from Binance API for a specified symbol and time range.

## Requirements
- Python 3.7 or higher
- requests
- pandas
- colorama

## Usage
1. Install the required packages using `pip install -r requirements.txt`
2. Update the script with your desired `symbol`, `interval`, `start_date`, `end_date`, and `round_decimal`.
3. Run the script using `python3 main.py`

## Output
The script generates a csv file with the name format `{symbol}_{start_date}_{end_date}_data.csv`.

## Parameters
- `symbol`: The trading symbol to collect data for, e.g., "BTCUSDT".
- `interval`: The time interval of each candlestick, e.g., "1d" for daily, "1h" for hourly, "1m" for minute, etc.
- `start_date`: The start date of the data collection in the format of a datetime object.
- `end_date`: The end date of the data collection in the format of a datetime object.
- `round_decimal`: The number of decimal places to round the collected data to.

## Data Collected

The script collects the following data for each candlestick:

| Parameter | English | 中文 |
| --- | --- | --- |
| Date | Date | 日期 |
| Open | Open price | 开盘价 |
| High | High price | 最高价 |
| Low | Low price | 最低价 |
| Close | Close price | 收盘价 |
| Volume | Trade volume | 成交量 |
| Bid1_Price | Best bid price | 买一价 |
| Bid2_Price | Second best bid price | 买二价 |
| Bid3_Price | Third best bid price | 买三价 |
| Bid4_Price | Fourth best bid price | 买四价 |
| Bid5_Price | Fifth best bid price | 买五价 |
| Bid1_Size | Best bid size | 买一量 |
| Bid2_Size | Second best bid size | 买二量 |
| Bid3_Size | Third best bid size | 买三量 |
| Bid4_Size | Fourth best bid size | 买四量 |
| Bid5_Size | Fifth best bid size | 买五量 |
| Ask1_Price | Best ask price | 卖一价 |
| Ask2_Price | Second best ask price | 卖二价 |
| Ask3_Price | Third best ask price | 卖三价 |
| Ask4_Price | Fourth best ask price | 卖四价 |
| Ask5_Price | Fifth best ask price | 卖五价 |
| Ask1_Size | Best ask size | 卖一量 |
| Ask2_Size | Second best ask size | 卖二量 |
| Ask3_Size | Third best ask size | 卖三量 |
| Ask4_Size | Fourth best ask size | 卖四量 |
| Ask5_Size | Fifth best ask size | 卖五量 |
| Buy_Volume | Total buy volume | 买入成交量 |
| Sell_Volume | Total sell volume | 卖出成交量 |
| Bid1_Size_Ratio | Best bid size ratio | 买一量占比 |
| Bid2_Size_Ratio | Second best bid size ratio | 买二量占比 |
| Bid3_Size_Ratio | Third best bid size ratio | 买三量占比 |
| Bid4_Size_Ratio | Fourth best bid size ratio | 买四量占比 |
| Bid5_Size_Ratio | Fifth best bid size ratio | 买五量占比 |
| Ask1_Size_Ratio | Best ask size ratio | 卖一量占比 |
| Ask2_Size_Ratio | Second best ask size ratio | 卖二量占比 |
| Ask3_Size_Ratio | Third best ask size ratio | 卖三量占比 |
| Ask4_Size_Ratio | Fourth best ask size ratio | 卖四量占比 |
| Ask5_Size_Ratio | Fifth best ask size ratio | 卖五量占比 |
| Buy_Spread | Buy spread | 买入价差 |
| Sell_Spread | Sell spread | 卖出价差 |
| Imbalance_Volume | Imbalance volume | 不平衡量 |
| WAP | Weighted average price | 加权平均价 |
| Trade_Diff | Trade price difference | 成交价差 |
| Trade_Spread | Trade price spread | 成交价差率 |

Note: Due to the rate limit and potential IP blocking imposed by Binance API, it is not feasible to use multiprocessing or multithreading for data processing. For the time being, we will perform requests sequentially in the main thread. Adding multiple proxy IPs or implementing delayed concurrency processing will not be considered at this time.
