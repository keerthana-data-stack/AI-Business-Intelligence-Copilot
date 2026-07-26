import streamlit as st
from frontend.ai_summary import render_ai_summary

from backend.charts import (
    create_bar_chart,
    create_line_chart,
    create_scatter_chart,
    create_box_plot,
    create_histogram,
    create_pie_chart,
    recommend_chart
)


def render_dashboard(df, profile):
    """
    Renders the dashboard page.
    """

    st.header("📊 Business Dashboard")

    if df is None:
        st.info("Please upload a dataset.")
        return

    if df.empty:
        st.warning("The uploaded dataset is empty.")
        return

    chart_type = st.selectbox(
        "Chart Type",
        [
            "Bar",
            "Line",
            "Scatter",
            "Histogram",
            "Box Plot",
            "Pie"
        ]
    )

    x_column = st.selectbox(
        "X Axis",
        df.columns
    )

    y_column = st.selectbox(
        "Y Axis",
        profile["numeric_columns"]
    )

    recommended = recommend_chart(
    x_column,
    y_column,
    profile
    )

    st.success(f"💡 Recommended Chart: {recommended}")

    try:
        if chart_type == "Bar":

            fig = create_bar_chart(df, x_column, y_column)

        elif chart_type == "Line":

            fig = create_line_chart(df, x_column, y_column)

        elif chart_type == "Scatter":

            fig = create_scatter_chart(df, x_column, y_column)

        elif chart_type == "Histogram":

            fig = create_histogram(df, y_column)

        elif chart_type == "Box Plot":

            fig = create_box_plot(df, y_column)

        else:

            fig = create_pie_chart(df, x_column, y_column)

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Unable to generate visualization.\n\n{e}")