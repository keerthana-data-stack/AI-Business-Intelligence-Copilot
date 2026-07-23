import streamlit as st

from backend.filters import apply_filters


def render_sidebar(df, profile):
    """
    Render sidebar filters and return filtered dataframe.
    """

    st.sidebar.subheader("🔍 Filters")

    selected_filters = {}

    for column in profile["categorical_columns"]:

        # Skip columns with too many unique values
        if df[column].nunique() <= 20:

            options = sorted(
                df[column]
                .dropna()
                .astype(str)
                .unique()
            )

            selected_values = st.sidebar.multiselect(
                label=column,
                options=options
            )

            if selected_values:

                selected_filters[column] = selected_values

    # Convert selected values back to strings before filtering
    if selected_filters:

        temp_df = df.copy()

        for column in selected_filters:
            temp_df[column] = temp_df[column].astype(str)

        df = apply_filters(temp_df, selected_filters)

    if st.sidebar.button("🗑️ Clear Filters"):
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.metric(
        "Rows after filtering",
        len(df)
    )

    return df