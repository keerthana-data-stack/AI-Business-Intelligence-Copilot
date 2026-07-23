def generate_insights(df, summary, quality, correlations):
    """
    Generate simple business insights.
    """

    insights = []

    insights.append(
        f"The dataset contains {summary['rows']:,} rows and {summary['columns']} columns."
    )

    if summary["missing"] > 0:
        insights.append(
            f"There are {summary['missing']:,} missing values in the dataset."
        )
    else:
        insights.append("No missing values were detected.")

    insights.append(
        f"Data Quality Score: {quality['score']}/100."
    )

    if correlations:

        strongest = correlations[0]

        insights.append(
            f"Strongest relationship: {strongest['column1']} and {strongest['column2']} "
            f"({strongest['correlation']})."
        )

    insights.append(
        f"{len(df):,} rows are currently displayed after filtering."
    )

    return insights