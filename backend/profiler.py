import pandas as pd


def profile_dataset(df):
    """
    Generate a complete profile of the uploaded dataset.
    Returns a dictionary containing useful metadata.
    """

    if df is None:
        return None

    profile = {
        "data_types": df.dtypes.astype(str),
        "missing_percent": (df.isnull().sum() / len(df) * 100).round(2),
        "unique_values": df.nunique(),
        "numeric_columns": df.select_dtypes(include="number").columns.tolist(),
        "categorical_columns": df.select_dtypes(exclude="number").columns.tolist(),
        "describe": df.describe(include="all").fillna("")
    }

    return profile