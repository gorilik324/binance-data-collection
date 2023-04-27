import requests
import pandas as pd
from datetime import datetime, timedelta
from colorama import Fore, Back, Style, init
init(autoreset=True)
import os

def get_klines(symbol, interval, start_time, end_time):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}"
    response = requests.get(url)
    klines = response.json()
    return klines

def get_depth(symbol, limit):
    url = f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit={limit}"
    response = requests.get(url)
    depth = response.json()
    return depth

def main():
    symbol = "BTCUSDT"
    interval = "1d"
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 4, 26)
    round_decimal = 8
    file_name = f"{symbol}_{start_date.strftime('%Y-%m-%d')}_{end_date.strftime('%Y-%m-%d')}_data.csv"
    
    data_list = []

    while start_date <= end_date:
        start_time = int(start_date.timestamp() * 1000)
        end_time = int((start_date + timedelta(days=1)).timestamp() * 1000)
        
        print(f"{Fore.YELLOW}Computing data for {start_date.strftime('%Y-%m-%d')}...")
        klines = get_klines(symbol, interval, start_time, end_time)
        depth = get_depth(symbol, 5)

        for kline in klines:
            timestamp, open, high, low, close, volume, _, _, _, _, _, _ = kline
            date = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')

            # Process depth data
            bids = depth['bids']
            asks = depth['asks']

            bid_prices = [float(bid[0]) for bid in bids]
            bid_sizes = [float(bid[1]) for bid in bids]
            ask_prices = [float(ask[0]) for ask in asks]
            ask_sizes = [float(ask[1]) for ask in asks]

            bid_total = sum(bid_sizes)
            ask_total = sum(ask_sizes)

            bid_size_ratios = [bid_size / bid_total for bid_size in bid_sizes]
            ask_size_ratios = [ask_size / ask_total for ask_size in ask_sizes]

            buy_spread = ask_prices[0] - bid_prices[0]
            sell_spread = bid_prices[0] - ask_prices[0]
            imbalance_volume = bid_total - ask_total
            wap = sum([price * size for price, size in zip(bid_prices, bid_sizes)]) / bid_total
            trade_diff = bid_prices[0] - ask_prices[0]
            trade_spread = trade_diff / ask_prices[0]

            data = [
                date, open, high, low, close, volume,
                *bid_prices, *bid_sizes, *ask_prices, *ask_sizes,
                round(bid_total, round_decimal), round(ask_total, round_decimal),
                *map(lambda x: round(x, round_decimal), bid_size_ratios),
                *map(lambda x: round(x, round_decimal), ask_size_ratios),
                round(buy_spread, round_decimal), round(sell_spread, round_decimal),
                round(imbalance_volume, round_decimal), round(wap, round_decimal),
                round(trade_diff, round_decimal), f"{trade_spread:.{round_decimal}f}"
            ]
            print(f"{Fore.GREEN}{data}")

            data_list.append(data)

        start_date += timedelta(days=1)

    columns = [
        "Date", "Open", "High", "Low", "Close", "Volume",
        "Bid1_Price", "Bid2_Price", "Bid3_Price", "Bid4_Price", "Bid5_Price",
        "Bid1_Size", "Bid2_Size", "Bid3_Size", "Bid4_Size", "Bid5_Size",
        "Ask1_Price", "Ask2_Price", "Ask3_Price", "Ask4_Price", "Ask5_Price",
        "Ask1_Size", "Ask2_Size", "Ask3_Size", "Ask4_Size", "Ask5_Size",
        "Buy_Volume", "Sell_Volume",
        "Bid1_Size_Ratio", "Bid2_Size_Ratio", "Bid3_Size_Ratio", "Bid4_Size_Ratio", "Bid5_Size_Ratio",
        "Ask1_Size_Ratio", "Ask2_Size_Ratio", "Ask3_Size_Ratio", "Ask4_Size_Ratio", "Ask5_Size_Ratio",
        "Buy_Spread", "Sell_Spread", "Imbalance_Volume", "WAP", "Trade_Diff", "Trade_Spread"
    ]

    df = pd.DataFrame(data_list, columns=columns)
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_csv(file_name, index=False)
    print(f"{Fore.RED} Data Saved.")

if __name__ == "__main__":
    main()
