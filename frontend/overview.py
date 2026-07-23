import streamlit as st


def render_overview(df, summary):
    """
    Render dataset overview cards.
    """

    st.subheader("📁 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    rows = summary["rows"]
    columns = summary["columns"]
    missing = summary["missing"]

    with col1:
        st.metric("Datasets", 1)

    with col2:
        st.metric("Rows", f"{rows:,}")

    with col3:
        st.metric("Columns", columns)

    with col4:
        st.metric("Missing Values", missing)

    st.divider()