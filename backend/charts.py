import plotly.express as px


def create_bar_chart(df, x_column, y_column):
    """
    Creates an interactive bar chart.
    """

    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )

    return fig


def create_line_chart(df, x_column, y_column):
    """
    Creates an interactive line chart.
    """

    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} over {x_column}"
    )

    return fig


def create_scatter_chart(df, x_column, y_column):
    """
    Creates an interactive scatter chart.
    """

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} vs {x_column}"
    )

    return fig

def create_histogram(df, column):

    return px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )

def create_box_plot(df, column):

    return px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )

def create_pie_chart(df, names, values):

    return px.pie(
        df,
        names=names,
        values=values,
        title=f"{values} by {names}"
    )


def recommend_chart(x_column, y_column, profile):
    """
    Recommend the best chart type based on the selected columns.
    """

    numeric = profile["numeric_columns"]
    categorical = profile["categorical_columns"]

    if x_column in categorical and y_column in numeric:
        return "Bar"

    if x_column in numeric and y_column in numeric:
        return "Scatter"

    return "Line"