import streamlit as st


def render_correlations(correlations):

    st.subheader("📈 Correlation Explorer")

    if not correlations:

        st.info("No strong correlations found.")
        return

    for item in correlations[:5]:

        if item["correlation"] > 0:

            st.success(
                f"{item['column1']} ↔ {item['column2']} : {item['correlation']}"
            )

        else:

            st.warning(
                f"{item['column1']} ↔ {item['column2']} : {item['correlation']}"
            )