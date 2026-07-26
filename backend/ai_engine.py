from anthropic import Anthropic

from config import (
    ANTHROPIC_API_KEY,
    MODEL,
    MAX_TOKENS,
    TEMPERATURE
)

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def generate_summary(context):
    prompt = build_summary_prompt(context)

    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return message.content[0].text

def build_context(summary, quality, correlations):
    return {
        "summary": {
            "rows": summary["rows"],
            "columns": summary["columns"],
            "missing": summary["missing"],
            "duplicates": summary["duplicates"],
        },
        "quality_score": quality,
        "correlations": correlations,
    }

def build_summary_prompt(context):
    return f"""
    You are a senior Business Intelligence Analyst.

    Using the dataset information below, write a concise executive summary.

    Dataset Information:

    Rows: {context['summary']['rows']}
    Columns: {context['summary']['columns']}
    Missing Values: {context['summary']['missing']}
    Duplicates: {context['summary']['duplicates']}
    Quality Score: {context['quality_score']}

    Strong Correlations:
    {context['correlations']}

    Requirements:
    - 4–6 sentences
    - Professional business language
    - Mention data quality
    - Mention important correlations
    - Mention any potential concerns
    - End with one actionable recommendation.
    """
def ask_ai(context, question):

    prompt = f"""
    You are an expert Business Intelligence Analyst.

    Dataset Context:

    {context}

    User Question:

    {question}

    Answer professionally and concisely.
    """

    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return message.content[0].text

def build_forecast_context(metrics, periods, frequency_label):
    """
    Builds context for the AI forecast summary.
    """

    return f"""
Historical Average: {metrics['Historical Average']}

Forecast Average: {metrics['Forecast Average']}

Expected Growth: {metrics['Growth (%)']}%

Forecast Horizon: {periods} {frequency_label.lower()}
"""

def build_forecast_prompt(context):
    return f"""
You are a business analyst.

Based on the forecast metrics below, write a short executive summary.

Requirements:
- 3 to 5 sentences
- Professional tone
- Mention whether the forecast indicates growth or decline
- Mention the forecast horizon
- Do not make up numbers
- Keep it concise

Forecast Information:

{context}
"""

def generate_forecast_summary(metrics, periods, frequency_label):

    context = build_forecast_context(
        metrics,
        periods,
        frequency_label
    )

    prompt = build_forecast_prompt(context)

    return ask_ai("", prompt)