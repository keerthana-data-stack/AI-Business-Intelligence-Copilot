import pandas as pd

# ----------------------------
# Column Role Constants
# ----------------------------

MEASURE = "measure"
DIMENSION = "dimension"
IDENTIFIER = "identifier"
DATE = "date"
RATE = "rate"

# ----------------------------
# Keyword Sets
# ----------------------------

IDENTIFIER_KEYWORDS = {
    "id",
    "code",
    "postal",
    "zip",
    "zipcode",
    "phone"
}

DATE_KEYWORDS = {
    "date",
    "time",
    "year",
    "month"
}

RATE_KEYWORDS = {
    "discount",
    "margin",
    "rate",
    "percent",
    "percentage"
}

MEASURE_KEYWORDS = {
    "sales",
    "profit",
    "revenue",
    "quantity",
    "cost",
    "price",
    "amount",
    "income",
    "expense"
}


# ----------------------------
# Helper Function
# ----------------------------

def contains_keyword(column_name, keywords):
    """
    Returns True if any keyword is found in the column name.
    """
    column_name = column_name.lower()

    return any(
        keyword in column_name
        for keyword in keywords
    )


# ----------------------------
# Column Classification
# ----------------------------

def classify_columns(df):
    """
    Classifies every column in the dataset into one of the following roles:

    - measure
    - dimension
    - identifier
    - date
    - rate

    Returns:
        dict
        {
            "Sales": "measure",
            "Region": "dimension",
            ...
        }
    """

    classification = {}

    for column in df.columns:

        # Datetime columns
        if (
            pd.api.types.is_datetime64_any_dtype(df[column])
            or contains_keyword(column, DATE_KEYWORDS)
        ):
            classification[column] = DATE

        # Identifier columns
        elif contains_keyword(column, IDENTIFIER_KEYWORDS):
            classification[column] = IDENTIFIER

        # Rate / Percentage columns
        elif contains_keyword(column, RATE_KEYWORDS):
            classification[column] = RATE

        # Known business measures
        elif contains_keyword(column, MEASURE_KEYWORDS):
            classification[column] = MEASURE

        # Unknown numeric columns are assumed to be measures
        elif pd.api.types.is_numeric_dtype(df[column]):
            classification[column] = MEASURE

        # Everything else is treated as a dimension
        else:
            classification[column] = DIMENSION

    return classification