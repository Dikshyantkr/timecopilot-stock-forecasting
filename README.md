\# 📈 Stock Price Forecasting using TimeCopilot



This project implements a multi-company stock price forecasting system using \*\*Time Series Analysis\*\*.  

It uses historical stock data from \*\*Yahoo Finance\*\*, forecasts future prices using \*\*AutoARIMA via TimeCopilot\*\*, and visualizes results through a \*\*Streamlit dashboard\*\*.



---



\## 🔧 Tech Stack

\- Python

\- TimeCopilot

\- AutoARIMA (StatsForecast)

\- Yahoo Finance (yfinance)

\- Streamlit

\- Pandas



---



\## 📊 Companies Covered (Indian Market)

RELIANCE, TCS, INFY, HDFCBANK, ICICIBANK, SBIN, AXISBANK,  

ITC, LT, HINDUNILVR, BAJFINANCE, BHARTIARTL, KOTAKBANK,  

ASIANPAINT, MARUTI, SUNPHARMA, TITAN, ULTRACEMCO, WIPRO, POWERGRID



---



\## ⚙️ Project Workflow

1\. Fetch historical stock data

2\. Clean and preprocess time-series data

3\. Forecast future prices (7 business days)

4\. Visualize forecasts using a web dashboard



---



\## ▶️ How to Run



```bash

pip install -r requirements.txt

python src/fetch\_data.py

python src/forecast\_multi.py

streamlit run app.py



