from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter

from reportlab.lib import colors

from tools.chart_generator import (
    generate_score_chart,
    generate_competitor_chart
)


# =========================================
# PDF EXPORTER
# =========================================

def export_pdf_report(

    report,

    output_path="ai_visibility_report.pdf"
):

    doc = SimpleDocTemplate(

        output_path,

        pagesize=letter,

        rightMargin=40,

        leftMargin=40,

        topMargin=40,

        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    story = []

    # =====================================
    # TITLE
    # =====================================

    title = Paragraph(

        "AI Visibility OS — Executive Intelligence Report",

        styles["Title"]
    )

    story.append(title)

    story.append(
        Spacer(1, 20)
    )

    # =====================================
    # SCORES
    # =====================================

    scores = report.get(
        "scores",
        {}
    )

    score_data = [

        [

            "SEO Score",

            "AI Visibility",

            "GEO/AEO",

            "Competitive Readiness"
        ],

        [

            scores.get(
                "seo_score",
                0
            ),

            scores.get(
                "ai_visibility_score",
                0
            ),

            scores.get(
                "geo_score",
                0
            ),

            scores.get(
                "competitive_readiness",
                0
            )
        ]
    ]

    table = Table(score_data)

    table.setStyle(

        TableStyle([

            (
                "BACKGROUND",

                (0, 0),

                (-1, 0),

                colors.HexColor("#111827")
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

    story.append(table)

    story.append(
        Spacer(1, 30)
    )

    # =====================================
    # SCORE CHART
    # =====================================

    score_chart = generate_score_chart(

        report.get(
            "scores",
            {}
        )
    )

    story.append(

        Image(

            score_chart,

            width=450,

            height=280
        )
    )

    story.append(
        Spacer(1, 30)
    )

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    story.append(

        Paragraph(

            "Executive Summary",

            styles["Heading1"]
        )
    )

    story.append(

        Paragraph(

            report.get(
                "executive_summary",
                ""
            ),

            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 24)
    )

    # =====================================
    # TECHNICAL AUDIT
    # =====================================

    story.append(

        Paragraph(

            "Technical SEO Audit",

            styles["Heading1"]
        )
    )

    technical_audit = report.get(
        "technical_audit",
        []
    )

    for finding in technical_audit:

        if not isinstance(
            finding,
            dict
        ):

            continue

        issue = finding.get(
            "issue",
            ""
        )

        details = finding.get(
            "details",
            ""
        )

        recommendation = finding.get(
            "recommendation",
            ""
        )

        priority = finding.get(
            "priority",
            "Medium"
        )

        text = f"""

        <b>{priority} — {issue}</b><br/><br/>

        {details}<br/><br/>

        <b>Recommendation:</b>
        {recommendation}

        """

        story.append(

            Paragraph(

                text,

                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 18)
        )

    # =====================================
    # GEO / AEO
    # =====================================

    story.append(

        Paragraph(

            "GEO / AEO Intelligence",

            styles["Heading1"]
        )
    )

    geo_analysis = report.get(
        "geo_aeo_analysis",
        []
    )

    for item in geo_analysis:

        if not isinstance(
            item,
            dict
        ):

            continue

        text = f"""

        <b>{item.get('status', '')}
        — {item.get('category', '')}</b><br/><br/>

        {item.get('details', '')}

        """

        story.append(

            Paragraph(

                text,

                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 18)
        )

    # =====================================
    # COMPETITOR BENCHMARKING
    # =====================================

    story.append(

        Paragraph(

            "Competitive Benchmarking",

            styles["Heading1"]
        )
    )

    competitors = report.get(
        "competitor_data",
        []
    )

    competitor_table = [

        [

            "Competitor",

            "SEO",

            "AI Visibility",

            "GEO/AEO",

            "Content Depth"
        ]
    ]

    for competitor in competitors:

        competitor_table.append([

            competitor.get(
                "name",
                ""
            ),

            competitor.get(
                "seo_score",
                0
            ),

            competitor.get(
                "ai_visibility",
                0
            ),

            competitor.get(
                "geo_score",
                0
            ),

            competitor.get(
                "content_depth",
                ""
            )
        ])

    competitor_table_obj = Table(
        competitor_table
    )

    competitor_table_obj.setStyle(

        TableStyle([

            (
                "BACKGROUND",

                (0, 0),

                (-1, 0),

                colors.HexColor("#111827")
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
            )
        ])
    )

    story.append(
        competitor_table_obj
    )

    story.append(
        Spacer(1, 30)
    )

    # =====================================
    # COMPETITOR CHART
    # =====================================

    competitor_chart = generate_competitor_chart(

        report.get(
            "competitor_data",
            []
        )
    )

    story.append(

        Image(

            competitor_chart,

            width=500,

            height=280
        )
    )

    story.append(
        Spacer(1, 30)
    )

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    story.append(

        Paragraph(

            "Strategic Recommendations",

            styles["Heading1"]
        )
    )

    story.append(

        Paragraph(

            report.get(
                "recommendations",
                ""
            ),

            styles["BodyText"]
        )
    )

    # =====================================
    # BUILD PDF
    # =====================================

    doc.build(story)

    return output_path