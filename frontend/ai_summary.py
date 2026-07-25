import streamlit as st

from backend.ai_engine import (
    build_context,
    generate_summary
)


def render_ai_summary(summary, quality, correlations):

    st.subheader("🤖 AI Executive Summary")

    if "ai_summary" not in st.session_state:
        st.session_state.ai_summary = None

    if st.button("Generate Executive Summary"):

        with st.spinner("Generating executive summary..."):

            context = build_context(
                summary,
                quality,
                correlations
            )

            st.session_state.ai_summary = generate_summary(context)

    if st.session_state.ai_summary:

        st.success(st.session_state.ai_summary)