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
from frontend.sidebar import render_sidebar
from frontend.analytics import render_analytics_page
from frontend.ai_assistant import render_ai_assistant
from frontend.cleaning_view import render_cleaning_page
from frontend.forecasting_view import render_forecasting_page
from frontend.settings import render_settings_page
from frontend.about import render_about_page

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
            "📊 Dashboard",
            "📁 Analytics",
            "🧹 Data Cleaning",
            "📈 Forecasting",
            "🤖 AI Assistant",
            "⚙️ Settings",
            "ℹ️ About"
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

# Load and analyze dataset only if a file is uploaded
uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

# Initialize variables
df = None
summary = None
profile = None

if uploaded_file is not None:

    file_bytes = uploaded_file.getvalue()

    if (
        "uploaded_file_bytes" not in st.session_state
        or st.session_state.uploaded_file_bytes != file_bytes
    ):

        try:
            st.session_state.df = load_dataset(uploaded_file)
            st.session_state.uploaded_file_bytes = file_bytes

        except Exception as e:
            st.error(f"Unable to load dataset.\n\n{e}")
            st.session_state.df = None

    df = st.session_state.df

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

# -------------------------
# PAGE ROUTING
# -------------------------

if page == "📊 Dashboard":

    if df is None:
        st.info("Upload a dataset first.")

    elif df.empty:
        st.warning("The uploaded dataset is empty.")

    else:
       render_analytics_page(
            df,
            summary,
            profile,
            kpis,
            quality,
            correlations,
            insights
        )

    render_dashboard(df, profile)

elif page == "📁 Analytics":
    render_upload_page(df, summary, profile)

elif page == "🤖 AI Assistant":
    if df is None:
        st.info("Upload a dataset first.")
    else:
        render_ai_assistant(
            df,
            summary,
            quality,
            correlations
        )

elif page == "🧹 Data Cleaning":
    if df is None:
        st.info("Upload a dataset first.")
    else:
        render_cleaning_page(df)

elif page == "📈 Forecasting":
    if df is None:
        st.info("Upload a dataset first.")
    else:
        render_forecasting_page(df)

elif page == "⚙️ Settings":
    render_settings_page(df)

elif page == "ℹ️ About":
    render_about_page()