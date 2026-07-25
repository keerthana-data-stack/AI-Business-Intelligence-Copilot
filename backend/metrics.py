from backend.column_classifier import (
    classify_columns,
    MEASURE,
    RATE
)


def generate_kpis(df):
    """
    Generate business-friendly KPIs based on column roles.
    """

    classification = classify_columns(df)

    kpis = []

    for column, role in classification.items():

        # Business measures
        if role == MEASURE:

            kpis.append({
                "title": f"Total {column}",
                "value": round(df[column].sum(), 2)
            })

            # Quantity usually doesn't need an average KPI
            if column.lower() != "quantity":
                kpis.append({
                    "title": f"Average {column}",
                    "value": round(df[column].mean(), 2)
                })

        # Rates/percentages
        elif role == RATE:

            kpis.append({
                "title": f"Average {column}",
                "value": round(df[column].mean(), 2)
            })

    return kpis