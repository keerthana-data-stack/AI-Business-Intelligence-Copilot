import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from backend.cleaning import find_column

def prepare_forecast_data(
        df,
        date_column,
        value_column,
        frequency="D"
    ):
    """
    Cleans and prepares data for forecasting.
    """

    date_column = find_column(df, date_column)
    value_column = find_column(df, value_column)

    if date_column is None:
        raise ValueError("Date column not found.")

    if value_column is None:
        raise ValueError("Value column not found.")

    cleaned = df[[date_column, value_column]].copy()

    cleaned[date_column] = pd.to_datetime(
        cleaned[date_column],
        errors="coerce"
    )

    cleaned[value_column] = pd.to_numeric(
        cleaned[value_column],
        errors="coerce"
    )

    cleaned = cleaned.dropna()

    cleaned = cleaned.sort_values(date_column)

    cleaned = (
        cleaned
        .set_index(date_column)
        .resample(frequency)[value_column]
        .sum()
        .reset_index()
    )
    return cleaned

def generate_forecast(
    prepared_df,
    periods,
    frequency="D"
):
    """
    Generates a forecast using Holt-Winters Exponential Smoothing.
    """

    if prepared_df is None or prepared_df.empty:
        return None, None

    date_column = prepared_df.columns[0]
    value_column = prepared_df.columns[1]

    model = ExponentialSmoothing(
        prepared_df[value_column],
        trend="add",
        seasonal=None
    )

    fitted_model = model.fit()

    predictions = fitted_model.forecast(periods)

    last_date = prepared_df[date_column].max()

    future_dates = pd.date_range(
        start=last_date,
        periods=periods + 1,
        freq=frequency
    )[1:]

    forecast_df = pd.DataFrame({
        date_column: future_dates,
        value_column: predictions.values
    })

    return prepared_df, forecast_df

def calculate_forecast_metrics(history_df, forecast_df):
    """
    Calculates summary metrics for the forecast.
    """

    if history_df is None or forecast_df is None:
        return {}

    value_column = history_df.columns[1]

    historical_average = history_df[value_column].mean()

    forecast_average = forecast_df[value_column].mean()

    growth = (
        (forecast_average - historical_average)
        / historical_average
    ) * 100

    return {
        "Historical Average": round(historical_average, 2),
        "Forecast Average": round(forecast_average, 2),
        "Growth (%)": round(growth, 2)
    }


