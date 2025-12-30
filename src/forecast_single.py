import pandas as pd
from timecopilot import TimeCopilotForecaster
from timecopilot.models.stats import AutoARIMA

# Load stock data
df = pd.read_csv("data/stocks/AAPL.csv")

# Rename columns
df = df.rename(columns={
    "Date": "ds",
    "Close": "y"
})

# Convert date to datetime
df["ds"] = pd.to_datetime(df["ds"])

# 🔑 FIX 1: Force y to numeric
df["y"] = pd.to_numeric(df["y"], errors="coerce")

# Clean data
df = df.dropna()
df = df.sort_values("ds")

# Required identifier
df["unique_id"] = "AAPL"

df = df[["unique_id", "ds", "y"]]

# Initialize forecaster
tcf = TimeCopilotForecaster(
    models=[AutoARIMA()]
)

# Run forecast (freq passed here)
forecast_df = tcf.forecast(
    df=df,
    h=14,
    freq="D"
)

print("Forecast output:")
print(forecast_df)
