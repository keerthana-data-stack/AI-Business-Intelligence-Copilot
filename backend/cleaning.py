import pandas as pd

def normalize(text):
    return str(text).strip().lower()


def find_column(df, column_name):
    """
    Finds a column name regardless of case.
    """

    column_name = normalize(column_name)

    for column in df.columns:
        if normalize(column) == column_name:
            return column

    return None

def get_missing_summary(df):
    """
    Returns the number of missing values in each column.
    """

    return df.isna().sum().to_dict()

def remove_duplicates(df):
    """
    Removes duplicate rows.
    """

    before = len(df)

    cleaned = df.drop_duplicates()

    removed = before - len(cleaned)

    return cleaned, removed

def drop_column(df, column):
    """
    Drops a column if it exists.
    """
    column = find_column(df, column)

    if column is None:
        return df, False

    return df.drop(columns=[column]), True

def fill_missing_values(df, column, method, value=None):
    """
    Fills missing values in the specified column.
    """
    method = normalize(method)
    column = find_column(df, column)

    if column is None:
        return df
    cleaned = df.copy()

    if method == "mean":
        fill_value = cleaned[column].mean()

    elif method == "median":
        fill_value = cleaned[column].median()

    elif method == "mode":
        mode = cleaned[column].mode()

        if mode.empty:
            return cleaned

        fill_value = mode.iloc[0]

    elif method == "constant":
        fill_value = value

    else:
        return cleaned

    cleaned[column] = cleaned[column].fillna(fill_value)

    return cleaned

def rename_column(df, old_name, new_name):

    old_name = find_column(df, old_name)

    if old_name is None:
        return df

    return df.rename(columns={old_name: new_name})

def convert_dtype(df, column, dtype):

    column = find_column(df, column)

    if column is None:
        return df

    dtype = normalize(dtype)

    cleaned = df.copy()

    try:

        if dtype == "int":
            cleaned[column] = cleaned[column].astype(int)

        elif dtype == "float":
            cleaned[column] = cleaned[column].astype(float)

        elif dtype == "string":
            cleaned[column] = cleaned[column].astype(str)

        elif dtype == "datetime":
            cleaned[column] = pd.to_datetime(cleaned[column])

    except Exception:
        return df

    return cleaned

