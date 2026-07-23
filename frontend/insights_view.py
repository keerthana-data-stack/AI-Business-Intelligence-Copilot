import streamlit as st


def render_insights(insights):

    st.subheader("🧠 Executive Insights")

    for insight in insights:

        st.info(insight)

    st.divider()