import streamlit as st

from backend.data_loader import load_dataset
from backend.data_cleaner import analyze_dataset
from backend.profiler import profile_dataset
from backend.filters import apply_filters

from frontend.dashboard import render_dashboard
from frontend.upload import render_upload_page
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
# FILE UPLOAD
# -------------------------

uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

# Initialize variables
df = None
summary = None
profile = None

# Load and analyze dataset only if a file is uploaded
if uploaded_file is not None:

    df = load_dataset(uploaded_file)

    if df is not None:
        summary = analyze_dataset(df)
        profile = profile_dataset(df)
        st.sidebar.subheader("🔍 Filters")

        selected_filters = {}

        for column in profile["categorical_columns"]:

            # Skip columns with too many unique values
            if df[column].nunique() <= 20:
                options = sorted(df[column].dropna().unique())

                selected_values = st.sidebar.multiselect(
                    label=column,
                    options=options
                )

                selected_filters[column] = selected_values
        # Apply filters
        df = apply_filters(df, selected_filters)

        # Clear Filters Button
        if st.sidebar.button("🗑️ Clear Filters"):
            st.rerun()

        # Show remaining rows
        st.sidebar.markdown("---")
        st.sidebar.metric(
            "Rows after filtering",
            len(df)
        )
# -------------------------
# KPI CARDS
# -------------------------

col1, col2, col3, col4 = st.columns(4)

rows = summary["rows"] if summary else 0
columns = summary["columns"] if summary else 0
missing = summary["missing"] if summary else 0

with col1:
    st.metric("Datasets", 1 if df is not None else 0)

with col2:
    st.metric("Rows", f"{rows:,}")

with col3:
    st.metric("Columns", columns)

with col4:
    st.metric("Missing Values", missing)

st.divider()

# -------------------------
# PAGE ROUTING
# -------------------------

if page == "Dashboard":
    render_dashboard(df, profile)

elif page == "Upload Data":
    render_upload_page(df, summary, profile)

elif page == "AI Assistant":
    st.header("🤖 AI Assistant")
    st.info("Coming soon...")

elif page == "Forecasting":
    st.header("📈 Forecasting")
    st.info("Coming soon...")

elif page == "Settings":
    st.header("⚙️ Settings")
    st.info("Coming soon...")