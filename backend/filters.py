def apply_filters(df, selected_filters):
    """
    Apply user-selected filters to a dataset.
    """

    filtered_df = df.copy()

    for column, values in selected_filters.items():

        if values:
            filtered_df = filtered_df[
                filtered_df[column].isin(values)
            ]

    return filtered_df