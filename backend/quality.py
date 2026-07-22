import pandas as pd


def calculate_quality_score(df):
    """
    Calculate a simple data quality score (0-100).
    """

    if df.empty:
        return {
            "score": 0,
            "missing_percent": 0,
            "duplicate_percent": 0
        }

    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isna().sum().sum()
    duplicate_rows = df.duplicated().sum()

    missing_percent = (missing_cells / total_cells) * 100
    duplicate_percent = (duplicate_rows / len(df)) * 100

    score = 100

    score -= missing_percent * 0.5
    score -= duplicate_percent * 0.5

    score = max(0, round(score, 1))

    return {
        "score": score,
        "missing_percent": round(missing_percent, 2),
        "duplicate_percent": round(duplicate_percent, 2)
    }