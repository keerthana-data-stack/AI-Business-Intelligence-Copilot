import pandas as pd
import re
from backend.column_classifier import (classify_columns, MEASURE, DIMENSION)

# --------------------------------------------------
# Supported Aggregations
# --------------------------------------------------

AGGREGATIONS = {
    "average": ("mean", "average"),
    "mean": ("mean", "average"),
    "sum": ("sum", "total"),
    "total": ("sum", "total"),
    "max": ("max", "maximum"),
    "maximum": ("max", "maximum"),
    "highest": ("max", "maximum"),
    "min": ("min", "minimum"),
    "minimum": ("min", "minimum"),
    "lowest": ("min", "minimum"),
    "count": ("count", "count")
}


# --------------------------------------------------
# Main Query Router
# --------------------------------------------------

def execute_query(df, question):
    """
    Executes analytical queries using Pandas.
    Returns None if the question is unsupported.
    """

    question = question.lower()

    handlers = [
        handle_missing_values,
        handle_duplicates,
        handle_ranking,
        handle_groupby,
        handle_filter,
        handle_aggregations,
        handle_dataset_info,
    ]

    for handler in handlers:

        result = handler(df, question)

        if result is not None:
            return result

    return None

# --------------------------------------------------
# helper functions
# --------------------------------------------------

def find_column(df, question):
    """
    Finds the first column mentioned in the user's question.
    """

    question = question.lower()

    for column in df.columns:
        if column.lower() in question:
            return column

    return None

def find_columns(df, question):
    """
    Finds all columns mentioned in the user's question.
    """

    question = question.lower()

    matches = []

    for column in df.columns:
        if column.lower() in question:
            matches.append(column)

    return matches

def find_number(question):
    """
    Finds the first number mentioned in the question.
    Defaults to 5 if none is found.
    """

    match = re.search(r"\d+", question)

    if match:
        return int(match.group())

    return 5

def find_dimension_value(df, question):

    question = question.lower()

    classification = classify_columns(df)

    for column, column_type in classification.items():

        if column_type != DIMENSION:
            continue

        values = df[column].dropna().unique()

        for value in values:

            value_str = str(value)

            if value_str.lower() in question:
                return column, value

    return None, None

# --------------------------------------------------
# Missing Values
# --------------------------------------------------

def handle_missing_values(df, question):

    if "missing" not in question:
        return None

    missing = df.isna().sum()
    missing = missing[missing > 0]

    if missing.empty:
        return "There are no missing values."

    return missing.to_string()


# --------------------------------------------------
# Duplicate Rows
# --------------------------------------------------

def handle_duplicates(df, question):

    if "duplicate" not in question:
        return None

    duplicates = df.duplicated().sum()

    return f"The dataset contains {duplicates} duplicate rows."

# --------------------------------------------------
# Ranking
# --------------------------------------------------

def handle_ranking(df, question):

    if "top" not in question and "bottom" not in question:
        return None

    column = find_column(df, question)

    if column is None:
        return None

    n = find_number(question)

    if "top" in question:
        values = df[column].nlargest(n)

        return (
            f"Top {n} {column} values:\n\n"
            + values.to_string(index=False)
        )

    if "bottom" in question:
        values = df[column].nsmallest(n)

        return (
            f"Bottom {n} {column} values:\n\n"
            + values.to_string(index=False)
        )

    return None

# --------------------------------------------------
# Group By
# --------------------------------------------------

def handle_groupby(df, question):

    if " by " not in question:
        return None

    columns = find_columns(df, question)

    if len(columns) < 2:
        return None

    classifications = classify_columns(df)

    measure = None
    dimension = None

    for column in columns:

        column_type = classifications.get(column)

        if column_type == MEASURE:
            measure = column

        elif column_type == DIMENSION:
            dimension = column

    if measure is None or dimension is None:
        return None

    method = "sum"
    label = "Total"

    for keyword, (agg_method, agg_label) in AGGREGATIONS.items():
        if keyword in question:
            method = agg_method
            label = agg_label.title()
            break

    result = (
        getattr(df.groupby(dimension)[measure], method)()
        .sort_values(ascending=False)
     )

    if result.dtype.kind == "f":
        result = result.round(2)

    return (
        f"{label} {measure} by {dimension}\n\n"
        + result.to_string()
    )

# --------------------------------------------------
# Filter
# --------------------------------------------------

def handle_filter(df, question):

    if " in " not in question and " for " not in question:
        return None

    measure = find_column(df, question)

    if measure is None:
        return None

    dimension, filter_value = find_dimension_value(df, question)

    filtered_df = df[df[dimension] == filter_value]

    method = "sum"
    label = "Total"

    for keyword, (agg_method, agg_label) in AGGREGATIONS.items():
        if keyword in question:
            method = agg_method
            label = agg_label.title()
            break

    result = getattr(filtered_df[measure], method)()

    if isinstance(result, float):
        result = round(result, 2)

    return (
        f"{label} {measure} for {dimension} = {filter_value}: {result}"
    )

# --------------------------------------------------
# Aggregations
# --------------------------------------------------

def handle_aggregations(df, question):

    column = find_column(df, question)

    if column is None:
        return None

    for keyword, (method, label) in AGGREGATIONS.items():

        if keyword in question:

            value = getattr(df[column], method)()

            if isinstance(value, float):
                value = round(value, 2)

            return f"The {label} {column} is {value}"

    return None

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

def handle_dataset_info(df, question):

    if "column names" in question or "list columns" in question:
        return ", ".join(df.columns)

    if "rows" in question and "duplicate" not in question:
        return f"The dataset contains {len(df)} rows."

    if "columns" in question:
        return f"The dataset contains {len(df.columns)} columns."

    return None