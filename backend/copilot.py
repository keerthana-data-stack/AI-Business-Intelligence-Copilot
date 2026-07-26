from backend.query_engine import execute_query
from backend.ai_engine import (
    ask_ai,
    build_context
)


def process_question(
    df,
    question,
    summary,
    quality,
    correlations
):
    """
    Processes a user's question using a hybrid
    AI + Pandas approach.
    """

    # Try Pandas first
    answer = execute_query(df, question)

    if answer is not None:
        return answer

    # Otherwise use Claude
    context = build_context(
        summary,
        quality,
        correlations
    )

    try:
        return ask_ai(
            context,
            question
        )

    except Exception as e:
        return f"Unable to contact the AI service.\n\n{e}"