from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter

from reportlab.platypus.tables import (
    Table,
    TableStyle
)

from reportlab.lib import colors


# =========================================
# PDF EXPORTER
# =========================================

def export_pdf(

    report_data,

    output_path="ai_visibility_report.pdf"
):

    # =====================================
    # DOCUMENT
    # =====================================

    doc = SimpleDocTemplate(

        output_path,

        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # =====================================
    # TITLE
    # =====================================

    title = Paragraph(

        "Executive AI Visibility Intelligence Report",

        styles["Title"]
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    # =====================================
    # SCORES
    # =====================================

    scores = report_data.get(
        "scores",
        {}
    )

    score_data = [

        ["Category", "Score"],

        [

            "SEO Maturity",

            str(
                scores.get(
                    "seo_score",
                    0
                )
            )
        ],

        [

            "AI Visibility",

            str(
                scores.get(
                    "ai_visibility_score",
                    0
                )
            )
        ],

        [

            "GEO / AEO",

            str(
                scores.get(
                    "geo_score",
                    0
                )
            )
        ],

        [

            "Competitive Readiness",

            str(
                scores.get(
                    "competitive_readiness",
                    0
                )
            )
        ]
    ]

    score_table = Table(
        score_data,
        colWidths=[250, 150]
    )

    score_table.setStyle(

        TableStyle([

            (

                "BACKGROUND",

                (0, 0),

                (-1, 0),

                colors.HexColor("#1f2937")
            ),

            (

                "TEXTCOLOR",

                (0, 0),

                (-1, 0),

                colors.white
            ),

            (

                "GRID",

                (0, 0),

                (-1, -1),

                1,

                colors.grey
            ),

            (

                "FONTNAME",

                (0, 0),

                (-1, 0),

                "Helvetica-Bold"
            ),

            (

                "BOTTOMPADDING",

                (0, 0),

                (-1, 0),

                12
            )
        ])
    )

    elements.append(score_table)

    elements.append(
        Spacer(1, 25)
    )

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    executive_summary = report_data.get(

        "executive_summary",

        "No executive summary available."
    )

    elements.append(

        Paragraph(

            "Executive Intelligence Summary",

            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(

        Paragraph(

            executive_summary,

            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 25)
    )

    # =====================================
    # TECHNICAL AUDIT
    # =====================================

    technical_audit = report_data.get(

        "technical_audit",

        []
    )

    elements.append(

        Paragraph(

            "Technical Audit Findings",

            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for item in technical_audit:

        if not isinstance(
            item,
            dict
        ):

            continue

        issue = item.get(
            "issue",
            ""
        )

        status = item.get(
            "status",
            ""
        )

        details = item.get(
            "details",
            ""
        )

        recommendation = item.get(
            "recommendation",
            ""
        )

        text = f"""

        <b>{issue}</b><br/>

        Status: {status}<br/>

        Details: {details}<br/>

        Recommendation: {recommendation}

        """

        elements.append(

            Paragraph(

                text,

                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

    # =====================================
    # GEO / AEO SECTION
    # =====================================

    geo_section = report_data.get(

        "geo_section",

        []
    )

    elements.append(

        Paragraph(

            "GEO / AEO Intelligence",

            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for item in geo_section:

        if not isinstance(
            item,
            dict
        ):

            continue

        category = item.get(
            "category",
            ""
        )

        status = item.get(
            "status",
            ""
        )

        details = item.get(
            "details",
            ""
        )

        text = f"""

        <b>{category}</b><br/>

        Status: {status}<br/>

        {details}

        """

        elements.append(

            Paragraph(

                text,

                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

    # =====================================
    # COMPETITOR SECTION
    # =====================================

    competitor_section = report_data.get(

        "competitor_section",

        {}
    )

    competitors = competitor_section.get(

        "competitors",

        []
    )

    elements.append(

        Paragraph(

            "Competitive Intelligence",

            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for competitor in competitors:

        if not isinstance(
            competitor,
            dict
        ):

            continue

        name = competitor.get(
            "name",
            "Unknown"
        )

        seo_score = competitor.get(
            "seo_score",
            0
        )

        ai_score = competitor.get(
            "ai_visibility",
            0
        )

        geo_score = competitor.get(
            "geo_score",
            0
        )

        text = f"""

        <b>{name}</b><br/>

        SEO Score: {seo_score}<br/>

        AI Visibility: {ai_score}<br/>

        GEO / AEO: {geo_score}

        """

        elements.append(

            Paragraph(

                text,

                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    recommendations = report_data.get(

        "recommendations",

        []
    )

    elements.append(

        Paragraph(

            "Strategic Recommendations",

            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    # =====================================
    # LIST / STRING SUPPORT
    # =====================================

    if isinstance(

        recommendations,

        list
    ):

        recommendation_lines = recommendations

    else:

        recommendation_lines = str(
            recommendations
        ).split("\n")

    for item in recommendation_lines:

        item = str(item).strip()

        if not item:

            continue

        elements.append(

            Paragraph(

                f"• {item}",

                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 8)
        )

    # =====================================
    # BUILD PDF
    # =====================================

    doc.build(elements)

    return output_path