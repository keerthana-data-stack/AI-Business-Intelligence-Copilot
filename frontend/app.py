import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Business Intelligence Copilot",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4149/4149640.png", width=120)

    st.title("Navigation")

    page = st.radio(
        "Go To",
        [
            "Dashboard",
            "Upload Data",
            "AI Assistant",
            "Forecasting",
            "Settings"
        ]
    )

# -------------------------
# HEADER
# -------------------------

st.title("📊 AI Business Intelligence Copilot")

st.caption("Your AI-powered business analytics assistant")

st.divider()

# -------------------------
# KPI CARDS
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Datasets", "0")

with col2:
    st.metric("Rows", "0")

with col3:
    st.metric("Columns", "0")

with col4:
    st.metric("Missing Values", "0")

st.divider()

# -------------------------
# PLACEHOLDERS
# -------------------------

left, right = st.columns([2,1])

with left:

    st.subheader("📈 Business Dashboard")

    st.info("Charts will appear here.")

with right:

    st.subheader("🤖 AI Insights")

    st.info("AI-generated insights will appear here.")

st.divider()

st.success("Dashboard Loaded Successfully 🚀")