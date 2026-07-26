import streamlit as st

def render_about_page():

    st.title("ℹ️ About")

    st.markdown("""
    ## AI Business Intelligence Copilot

    AI Business Intelligence Copilot is an interactive analytics platform
    that helps users explore, clean, analyze, forecast, and gain AI-powered
    insights from business datasets.

    The application combines traditional Business Intelligence techniques
    with Generative AI to support faster and smarter decision making.
    """)
    st.divider()

    st.subheader("✨ Features")

    st.markdown("""
    - 📊 Interactive Dashboard
    - 📈 Business Analytics
    - 🧹 Data Cleaning
    - 🔮 Sales Forecasting
    - 🤖 AI Assistant
    - 📥 Forecast Export
    """)
    st.divider()

    st.subheader("🛠️ Technology Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
    **Frontend**
    - Streamlit

    **Programming**
    - Python
    - Pandas
    - NumPy
    """)

    with col2:
        st.markdown("""
    **Visualization**
    - Matplotlib

    **Machine Learning**
    - Statsmodels

    **AI**
    - Anthropic Claude
    """)
    st.divider()

    st.subheader("🏗️ Architecture")

    st.code("""
    Upload Dataset
        │
        ▼
    Data Loader
        │
        ▼
    Data Profiler
         │
    ┌────┼───────────────┐
    ▼    ▼       ▼       ▼
    Dashboard Analytics Cleaning Forecasting
                    │
                    ▼
            AI Assistant
    """)
    st.divider()

    st.subheader("🚀 Future Enhancements")

    st.markdown("""
    - Power BI Integration
    - Salesforce CRM Integration
    - Automated PDF Reports
    - Scheduled Forecasting
    - Multi-user Authentication
    - Cloud Deployment
    """)
    st.divider()

    st.subheader("👩‍💻 Developer")

    st.markdown("""
    **Keerthana Singaravel**

    Master of Science in Business Analytics

    Seattle University

    2026
    """)
    st.caption("Version 1.0")