import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Stock Forecast Dashboard", layout="centered")

st.title("📈 Stock Price Forecast Dashboard")
st.write("Time Series Forecasting using TimeCopilot (AutoARIMA)")

forecast_dir = "data/forecasts"

# Load combined forecast
forecast_file = os.path.join(forecast_dir, "forecast_all_companies.csv")

if not os.path.exists(forecast_file):
    st.error("Forecast file not found. Run backend first.")
    st.stop()

df = pd.read_csv(forecast_file)

# Company selector
companies = sorted(df["unique_id"].unique())
company = st.selectbox("Select Company", companies)

# Filter data
company_df = df[df["unique_id"] == company]

st.subheader(f"📊 7-Day Forecast for {company}")
st.line_chart(company_df.set_index("ds")["AutoARIMA"])

st.dataframe(company_df)
