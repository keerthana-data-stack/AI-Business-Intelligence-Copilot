import pandas as pd


def find_correlations(df):
    """
    Find strong positive and negative correlations
    between numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return []

    corr_matrix = numeric_df.corr()

    insights = []

    columns = corr_matrix.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):

            value = corr_matrix.iloc[i, j]

            if abs(value) >= 0.70:

                insights.append({
                    "column1": columns[i],
                    "column2": columns[j],
                    "correlation": round(value, 2)
                })

    insights.sort(
        key=lambda x: abs(x["correlation"]),
        reverse=True
    )

    return insights