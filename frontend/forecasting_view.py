import streamlit as st
import matplotlib.pyplot as plt
from backend.profiler import profile_dataset 
from backend.forecasting import (
    prepare_forecast_data,
    generate_forecast,
    calculate_forecast_metrics
)
from backend.ai_engine import generate_forecast_summary
from datetime import datetime

def render_forecasting_page(df):

    st.title("📈 Forecasting")

    if df is None:
        st.info("Please upload a dataset first.")
        return

    profile = profile_dataset(df)

    date_columns = profile["date_columns"]
    measure_columns = profile["measure_columns"]

    if not date_columns:
        st.warning("No date columns found.")
        return

    if not measure_columns:
        st.warning("No measure columns found.")
        return

    date_column = st.selectbox(
            "Date Column",
            date_columns
        )

    value_column = st.selectbox(
            "Measure",
            measure_columns
        )

    frequency_label = st.selectbox(
        "Aggregation Level",
        ["Daily", "Weekly", "Monthly"],
        index=2
    )

    frequency_map = {
        "Daily": "D",
        "Weekly": "W",
        "Monthly": "MS"
    }

    frequency = frequency_map[frequency_label]

    periods = st.selectbox(
            "Forecast Horizon",
            [7, 30, 90],
            index=1
        )

    try:

        prepared = prepare_forecast_data(
            df,
            date_column,
            value_column,
            frequency
        )

        history, forecast = generate_forecast(
            prepared,
            periods,
            frequency
        )

        metrics = calculate_forecast_metrics(
            history,
            forecast
        )

    except Exception as e:

        st.error(f"Unable to generate forecast.\n\n{e}")
        return

    if len(prepared) < 5:
        st.warning(
            "Not enough historical data to generate a reliable forecast."
        )
        return

    st.subheader("Forecast Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Historical Average",
        metrics["Historical Average"]
    )

    col2.metric(
        "Forecast Average",
        metrics["Forecast Average"]
    )

    col3.metric(
        "Growth",
        f'{metrics["Growth (%)"]}%',
        delta=f'{metrics["Growth (%)"]}%'
    )

    st.markdown("### Forecast Details")

    col1, col2 = st.columns(2)

    col1.write(f"**Historical Records:** {len(history)}")
    col1.write(f"**Forecast Periods:** {len(forecast)}")

    col2.write(f"**Last Historical Date:** {history.iloc[-1, 0].date()}")
    col2.write(f"**Last Forecast Date:** {forecast.iloc[-1, 0].date()}")

    st.subheader("Forecast")

    fig, ax = plt.subplots(figsize=(12, 5))

    # Historical data
    ax.plot(
        history.iloc[:, 0],
        history.iloc[:, 1],
        label="History",
        linewidth=2
    )

    # Forecast
    ax.plot(
        forecast.iloc[:, 0],
        forecast.iloc[:, 1],
        "--",
        linewidth=2,
        label="Forecast"
    )

    # Vertical separator
    ax.axvline(
        history.iloc[-1, 0],
        linestyle=":",
        linewidth=2,
        color="gray",
        label="Forecast Start"
    )

    ax.set_title(f"{value_column} Forecast")

    ax.set_xlabel(date_column)
    ax.set_ylabel(value_column)

    ax.grid(alpha=0.3)

    ax.legend()

    st.pyplot(fig)

    st.subheader("🤖 AI Forecast Summary")

    if st.button("Generate AI Forecast Summary"):

        with st.spinner("Analyzing forecast..."):

            summary = generate_forecast_summary(
                metrics,
                periods,
                frequency_label
            )

            st.success(summary)

    st.subheader("Forecast Data")
    st.dataframe(forecast)
    filename = (
        f"{value_column.lower().replace(' ', '_')}"
        f"_forecast_"
        f"{datetime.today().strftime('%Y%m%d')}.csv"
    )

    csv = forecast.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Forecast",
        data=csv,
        file_name=filename,
        mime="text/csv"
    )