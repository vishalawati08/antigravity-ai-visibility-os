from fpdf import FPDF


def safe_text(text):

    if not text:
        return ""

    text = str(text)

    # Remove unsupported characters
    text = text.encode(
        "latin-1",
        "replace"
    ).decode("latin-1")

    # Prevent huge unbreakable strings
    if len(text) > 500:
        text = text[:500] + "..."

    return text


def generate_report(
    result,
    filename="seo_audit_report.pdf"
):

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.add_page()

    # ====================================
    # TITLE
    # ====================================

    pdf.set_font("Arial", "B", 20)

    pdf.cell(
        190,
        10,
        "AI SEO Strategist Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    # ====================================
    # EXECUTIVE SUMMARY
    # ====================================

    pdf.set_font("Arial", "B", 16)

    pdf.cell(
        190,
        10,
        "Executive Summary",
        ln=True
    )

    pdf.set_font("Arial", "", 12)

    pdf.multi_cell(
        190,
        8,
        safe_text(
            result["executive_summary"]
        )
    )

    pdf.ln(5)

    # ====================================
    # SEO METRICS
    # ====================================

    pdf.set_font("Arial", "B", 16)

    pdf.cell(
        190,
        10,
        "SEO Metrics",
        ln=True
    )

    pdf.set_font("Arial", "", 12)

    metrics = [
        f"SEO Score: {result['seo_score']}/100",
        f"GEO Score: {result['geo_score']}/100",
        f"Word Count: {result['word_count']}",
        f"Total Links: {result['total_links']}",
        f"Images: {result['total_images']}",
        f"Schema Found: {result['schema_found']}"
    ]

    for metric in metrics:

        pdf.multi_cell(
            190,
            8,
            safe_text(metric)
        )

    pdf.ln(5)

    # ====================================
    # STRATEGIC INSIGHTS
    # ====================================

    pdf.set_font("Arial", "B", 16)

    pdf.cell(
        190,
        10,
        "Strategic Insights",
        ln=True
    )

    pdf.set_font("Arial", "", 12)

    for insight in result["strategic_insights"]:

        pdf.multi_cell(
            190,
            8,
            safe_text(f"- {insight}")
        )

    pdf.ln(5)

    # ====================================
    # PRIORITY ACTIONS
    # ====================================

    pdf.set_font("Arial", "B", 16)

    pdf.cell(
        190,
        10,
        "Priority Actions",
        ln=True
    )

    pdf.set_font("Arial", "", 12)

    for action in result["priority_actions"]:

        pdf.multi_cell(
            190,
            8,
            safe_text(f"- {action}")
        )

    pdf.ln(5)

    # ====================================
    # SERP INSIGHTS
    # ====================================

    pdf.set_font("Arial", "B", 16)

    pdf.cell(
        190,
        10,
        "SERP Intelligence",
        ln=True
    )

    pdf.set_font("Arial", "", 12)

    for insight in result["serp_insights"]:

        pdf.multi_cell(
            190,
            8,
            safe_text(f"- {insight}")
        )

    pdf.ln(5)

    # ====================================
    # TOP RANKING URLS
    # ====================================

    pdf.set_font("Arial", "B", 16)

    pdf.cell(
        190,
        10,
        "Top Ranking URLs",
        ln=True
    )

    pdf.set_font("Arial", "", 11)

    for url in result["serp_results"][:10]:

        pdf.multi_cell(
            190,
            7,
            safe_text(url)
        )

    # ====================================
    # SAVE PDF
    # ====================================

    pdf.output(filename)

    return filename