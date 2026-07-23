import streamlit as st


def render_kpis(kpis):

    if not kpis:
        return

    st.subheader("📊 Key Performance Indicators")

    cols = st.columns(min(4, len(kpis)))

    for i, kpi in enumerate(kpis[:4]):

        cols[i].metric(
            kpi["title"],
            f"{kpi['value']:,}"
        )

    st.divider()