import os
import pandas as pd

from timecopilot import TimeCopilotForecaster
from timecopilot.models.stats import AutoARIMA


def main():
    data_dir = "data/stocks"
    out_dir = "data/forecasts"
    os.makedirs(out_dir, exist_ok=True)

    csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

    print("Found", len(csv_files), "companies")

    all_forecasts = []

    for file in csv_files:
        ticker = file.replace(".csv", "")
        print(f"\nForecasting {ticker}")

        df = pd.read_csv(os.path.join(data_dir, file))

        # Prepare data
        df = df[["Date", "Close"]].copy()
        df.rename(columns={"Date": "ds", "Close": "y"}, inplace=True)

        df["ds"] = pd.to_datetime(df["ds"])
        df["y"] = pd.to_numeric(df["y"], errors="coerce")
        df = df.dropna()

        df["unique_id"] = ticker
        df = df[["unique_id", "ds", "y"]]

        # Forecaster (single series → no multiprocessing)
        tcf = TimeCopilotForecaster(
            models=[AutoARIMA()]
        )

        forecast = tcf.forecast(
            df=df,
            h=7,
            freq="B"
        )

        forecast.to_csv(
            f"{out_dir}/{ticker}_forecast.csv",
            index=False
        )

        all_forecasts.append(forecast)

    # Combine all forecasts
    final_df = pd.concat(all_forecasts, ignore_index=True)
    final_df.to_csv(
        f"{out_dir}/forecast_all_companies.csv",
        index=False
    )

    print("\n✅ Forecasting completed for all companies")
    print(final_df.head())


if __name__ == "__main__":
    main()
