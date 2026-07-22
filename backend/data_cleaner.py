import pandas as pd


def analyze_dataset(df):
    """
    Returns useful statistics about the dataset.
    """

    if df is None:
        return None

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": df.isna().sum().sum(),
        "duplicates": df.duplicated().sum(),
        "memory": round(df.memory_usage(deep=True).sum() / 1024, 2)
    }

    return summary