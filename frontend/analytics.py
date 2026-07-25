from frontend.overview import render_overview
from frontend.kpi import render_kpis
from frontend.quality import render_quality
from frontend.correlation_view import render_correlations
from frontend.insights_view import render_insights
from frontend.ai_summary import render_ai_summary

def render_analytics_page(
    df,
    summary,
    profile,
    kpis,
    quality,
    correlations,
    insights
):

    render_overview(df, summary)

    render_kpis(kpis)

    render_quality(quality)

    render_correlations(correlations)

    render_insights(insights)

    render_ai_summary(
        summary,
        quality,
        correlations
    )