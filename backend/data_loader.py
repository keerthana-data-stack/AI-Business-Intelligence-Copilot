import pandas as pd


def load_dataset(uploaded_file):
    """
    Loads a CSV or Excel dataset and returns a pandas DataFrame.
    """

    if uploaded_file is None:
        return None

    try:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        else:
            return None

        return df

    except Exception:
        return None