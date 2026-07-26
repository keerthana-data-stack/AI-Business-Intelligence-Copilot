import streamlit as st
from config import MODEL, TEMPERATURE, MAX_TOKENS

def render_settings_page(df):

    st.title("⚙️ Settings")
    st.subheader("Application Settings")

    if "default_frequency" not in st.session_state:
        st.session_state.default_frequency = "Monthly"

    if "default_horizon" not in st.session_state:
        st.session_state.default_horizon = 6

    frequency = st.selectbox(
        "Default Forecast Aggregation",
        ["Daily", "Weekly", "Monthly"],
        index=["Daily", "Weekly", "Monthly"].index(
            st.session_state.default_frequency
        )
    )

    if frequency == "Daily":
        horizon_options = [7, 30, 90]

    elif frequency == "Weekly":
        horizon_options = [4, 8, 12]

    else:  # Monthly
        horizon_options = [3, 6, 12]

    horizon = st.selectbox(
        "Default Forecast Horizon",
        horizon_options,
        index=0
    )

    st.session_state.default_frequency = frequency
    st.session_state.default_horizon = horizon

    st.divider()

    st.subheader("🤖 AI Configuration")

    st.write(f"**Model:** {MODEL}")
    st.write(f"**Temperature:** {TEMPERATURE}")
    st.write(f"**Max Tokens:** {MAX_TOKENS}")

    st.divider()

    st.subheader("📊 Current Dataset")

    if df is None:

        st.info("No dataset uploaded.")

    else:
        col1, col2 = st.columns(2)

        col1.metric("Rows", len(df))
        col1.metric("Columns", len(df.columns))

        memory = round(df.memory_usage(deep=True).sum() / (1024**2), 2)

        col2.metric("Memory (MB)", memory)
        col2.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    st.divider()

    st.subheader("Application")

    st.write("**Name:** AI Business Intelligence Copilot")
    st.write("**Version:** 1.0")

    st.write("### Technologies")

    st.markdown("""
    - Python
    - Streamlit
    - Pandas
    - Matplotlib
    - Statsmodels
    - Anthropic Claude
    """)