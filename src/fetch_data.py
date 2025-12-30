import pandas as pd
import yfinance as yf
import os

# Paths
COMPANY_CSV = "data/company_list.csv"
SAVE_DIR = "data/stocks"

os.makedirs(SAVE_DIR, exist_ok=True)

# Load Indian tickers
companies = pd.read_csv(COMPANY_CSV)
tickers = companies["ticker"].tolist()

for ticker in tickers:
    print(f"Fetching {ticker}")
    df = yf.download(ticker, start="2018-01-01", progress=False)

    if df.empty:
        print(f"⚠️ No data for {ticker}")
        continue

    df.reset_index(inplace=True)
    df.to_csv(f"{SAVE_DIR}/{ticker}.csv", index=False)

print("Indian stock data download complete")
