import streamlit as st


def render_quality(quality):

    st.subheader("🛡️ Data Quality")

    score = quality["score"]

    if score >= 90:
        color = "🟢"
    elif score >= 70:
        color = "🟡"
    else:
        color = "🔴"

    st.metric(
        "Data Quality Score",
        f"{color} {score}/100"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Missing %",
            f"{quality['missing_percent']}%"
        )

    with col2:
        st.metric(
            "Duplicate %",
            f"{quality['duplicate_percent']}%"
        )

    st.divider()