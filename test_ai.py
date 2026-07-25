import pandas as pd


df = pd.read_csv(r"C:\Users\keert\OneDrive\Desktop\PG\Projects\Finance\archive\SampleSuperstore.csv")

def fill_missing_values(df, column, method, value=None):
    """
    Fills missing values in the specified column.
    """

    if column not in df.columns:
        return df

    cleaned = df.copy()

    if method == "Mean":
        fill_value = cleaned[column].mean()

    elif method == "Median":
        fill_value = cleaned[column].median()

    elif method == "Mode":
        fill_value = cleaned[column].mode().iloc[0]

    elif method == "Constant":
        fill_value = value

    else:
        return cleaned

    cleaned[column] = cleaned[column].fillna(fill_value)

    return cleaned

print(df["Sales"].isna().sum())

clean_df = fill_missing_values(df, "Sales", "Constant", 0)

print(clean_df["Sales"].isna().sum())