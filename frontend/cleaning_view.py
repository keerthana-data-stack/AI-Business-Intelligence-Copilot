import streamlit as st

from backend.cleaning import (
    get_missing_summary,
    fill_missing_values,
    remove_duplicates,
    drop_column,
    rename_column,
    convert_dtype
)

def render_cleaning_page(df):

    st.title("🧹 Data Cleaning")

    if df is None:
        st.info("Please upload a dataset first.")
        return
    df = st.session_state.df

    st.subheader("Dataset Summary")

    summary = get_missing_summary(df)

    total_missing = sum(summary.values())

    duplicate_count = len(df) - len(df.drop_duplicates())

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing Values", total_missing)
    col4.metric("Duplicate Rows", duplicate_count)

    st.divider()

    st.subheader("Fill Missing Values")

    column = st.selectbox(
        "Column",
        df.columns,
        key="fill_column"
    )

    method = st.selectbox(
        "Method",
        ["Mean", "Median", "Mode", "Constant"],
        key="fill_method"
    )

    value = None

    if method == "Constant":
        value = st.text_input("Constant Value")
    if st.button("Fill Missing Values"):

        st.session_state.df = fill_missing_values(
            st.session_state.df,
            column,
            method,
            value
        )

        st.success("Missing values filled.")

    st.divider()

    st.subheader("Remove Duplicates")

    if st.button("Remove Duplicates"):

        cleaned_df, removed = remove_duplicates(
            st.session_state.df
        )

        st.session_state.df = cleaned_df

        st.success(f"Removed {removed} duplicate rows.")

    st.divider()

    st.subheader("Rename Column")

    old_name = st.selectbox(
        "Current Column",
        df.columns,
        key="rename_old"
    )

    new_name = st.text_input(
        "New Column Name",
        key="rename_new"
    )

    if st.button("Rename Column"):

        st.session_state.df = rename_column(
            st.session_state.df,
            old_name,
            new_name
        )

        st.success("Column renamed successfully.")

    st.divider()

    st.subheader("Convert Data Type")

    dtype_column = st.selectbox(
        "Column",
        df.columns,
        key="dtype_column"
    )

    dtype = st.selectbox(
        "New Type",
        ["int", "float", "string", "datetime"],
        key="dtype"
    )

    if st.button("Convert Data Type"):

        st.session_state.df = convert_dtype(
            st.session_state.df,
            dtype_column,
            dtype
        )

        st.success("Data type updated.")

    st.divider()

    st.subheader("Drop Column")

    drop_col = st.selectbox(
        "Select Column",
        df.columns,
        key="drop_column"
    )

    if st.button("Drop Column"):

        cleaned_df, success = drop_column(
            st.session_state.df,
            drop_col
        )

        if success:
            st.session_state.df = cleaned_df
            st.success(f"{drop_col} removed successfully.")
        else:
            st.error("Column not found.")

    st.divider()

    st.subheader("Preview")

    st.dataframe(
        st.session_state.df,
        use_container_width=True
    )

    csv = st.session_state.df.to_csv(index=False)

    st.download_button(
        "Download Cleaned Dataset",
        csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )