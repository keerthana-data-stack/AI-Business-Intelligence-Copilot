import streamlit as st


def render_upload_page(df, summary, profile):
    """
    Renders the upload and data profiling page.
    """

    st.header("📁 Analytics & Data Profile")

    if df is None:
        st.info("Upload a dataset to begin.")
        return

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows:", summary["rows"])
        st.write("Columns:", summary["columns"])

    with col2:
        st.write("Memory Usage (KB):", summary["memory"])
        st.write("Duplicate Rows:", summary["duplicates"])

    st.divider()

    st.subheader("📋 Data Profile")

    st.write("### Data Types")
    st.dataframe(profile["data_types"])

    st.write("### Missing Values (%)")
    st.dataframe(profile["missing_percent"])

    st.write("### Unique Values")
    st.dataframe(profile["unique_values"])

    st.write("### Numeric Columns")
    st.write(profile["numeric_columns"])

    st.write("### Categorical Columns")
    st.write(profile["categorical_columns"])

    st.write("### Statistical Summary")
    st.dataframe(profile["describe"])