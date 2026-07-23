import streamlit as st

from backend.data_loader import load_dataset
from backend.data_summary import analyze_dataset
from backend.profiler import profile_dataset
from backend.filters import apply_filters
from backend.metrics import generate_kpis
from backend.quality import calculate_quality_score
from backend.correlation import find_correlations
from backend.insights import generate_insights

from frontend.dashboard import render_dashboard
from frontend.upload import render_upload_page
from frontend.overview import render_overview
from frontend.kpi import render_kpis
from frontend.quality import render_quality
from frontend.correlation_view import render_correlations
from frontend.insights_view import render_insights
from frontend.sidebar import render_sidebar
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
        original_df = df.copy()
        summary = analyze_dataset(df)
        profile = profile_dataset(df)
        df = render_sidebar(df, profile)

        kpis = generate_kpis(df)

        quality = calculate_quality_score(original_df)

        correlations = find_correlations(df)

        insights = generate_insights(
            df,
            summary,
            quality,
            correlations
        )

        render_overview(df, summary)

        render_kpis(kpis)

        render_quality(quality)

        render_correlations(correlations)

        render_insights(insights)
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