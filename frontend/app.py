import streamlit as st

# Configure page
st.set_page_config(
    page_title="AI Business Intelligence Copilot",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 AI Business Intelligence Copilot")

st.markdown("""
Welcome!

This application will help businesses:

- Upload datasets
- Analyze sales
- Generate charts
- Ask AI questions
- Forecast future trends
- Generate executive reports
""")

st.success("Project setup completed successfully! 🚀")

st.metric(
    label="Datasets Uploaded",
    value=0
)