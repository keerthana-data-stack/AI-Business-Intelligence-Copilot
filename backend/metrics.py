import pandas as pd


def generate_kpis(df):
    """
    Generate KPI metrics from numeric columns.
    """

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if not numeric_columns:
        return []

    kpis = []

    for column in numeric_columns:

        kpis.append({
            "title": f"Total {column}",
            "value": round(df[column].sum(), 2)
        })

        kpis.append({
            "title": f"Average {column}",
            "value": round(df[column].mean(), 2)
        })

    return kpis