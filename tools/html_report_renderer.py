# =========================================
# HTML REPORT RENDERER
# =========================================

def render_html_report(report):

    scores = report.get(
        "scores",
        {}
    )

    executive_summary = report.get(
        "executive_summary",
        ""
    )

    technical_audit = report.get(
        "technical_audit",
        []
    )

    geo_aeo_analysis = report.get(
        "geo_aeo_analysis",
        []
    )

    competitor_data = report.get(
        "competitor_data",
        []
    )

    serp_analysis = report.get(
        "serp_analysis",
        ""
    )

    recommendations = report.get(
        "recommendations",
        ""
    )

    # =====================================
    # SCORE HELPERS
    # =====================================

    def build_score_bar(score):

        color = "#DC2626"

        if score >= 80:

            color = "#16A34A"

        elif score >= 60:

            color = "#F59E0B"

        return f"""

        <div class="score-bar-bg">

            <div class="score-bar-fill"
                style="
                    width:{score}%;
                    background:{color};
                ">

            </div>

        </div>

        """

    # =====================================
    # TECHNICAL AUDIT
    # =====================================

    audit_html = ""

    for finding in technical_audit:

        if not isinstance(
            finding,
            dict
        ):

            continue

        priority = finding.get(
            "priority",
            "Medium"
        )

        color = "#F59E0B"

        if priority == "Critical":

            color = "#DC2626"

        elif priority == "High":

            color = "#EA580C"

        elif priority == "Low":

            color = "#16A34A"

        audit_html += f"""

        <div class="audit-card">

            <div class="audit-top">

                <span class="pill"
                    style="background:{color};">

                    {priority}

                </span>

                <span class="audit-category">

                    {finding.get('category', '')}

                </span>

            </div>

            <div class="audit-title">

                {finding.get('issue', '')}

            </div>

            <div class="audit-details">

                {finding.get('details', '')}

            </div>

            <div class="audit-recommendation">

                <strong>Recommendation:</strong>

                {finding.get('recommendation', '')}

            </div>

        </div>
        """

    # =====================================
    # GEO / AEO
    # =====================================

    geo_html = ""

    for item in geo_aeo_analysis:

        if not isinstance(
            item,
            dict
        ):

            continue

        status = item.get(
            "status",
            "Analysis"
        )

        color = "#6366F1"

        if status == "Positive":

            color = "#16A34A"

        elif status == "Risk":

            color = "#DC2626"

        elif status == "Opportunity":

            color = "#F59E0B"

        geo_html += f"""

        <div class="geo-card">

            <div class="geo-top">

                <span class="pill"
                    style="background:{color};">

                    {status}

                </span>

                <span class="geo-category">

                    {item.get('category', '')}

                </span>

            </div>

            <div class="geo-details">

                {item.get('details', '')}

            </div>

        </div>
        """

    # =====================================
    # COMPETITOR TABLE
    # =====================================

    competitor_html = ""

    top_score = 0

    for competitor in competitor_data:

        if competitor.get(
            "seo_score",
            0
        ) > top_score:

            top_score = competitor.get(
                "seo_score",
                0
            )

    for competitor in competitor_data:

        leader = ""

        if competitor.get(
            "seo_score",
            0
        ) == top_score:

            leader = """

            <span class="leader-pill">
                Leader
            </span>

            """

        competitor_html += f"""

        <tr>

            <td>
                {competitor.get('name', '')}
                {leader}
            </td>

            <td>
                {competitor.get('seo_score', 0)}
            </td>

            <td>
                {competitor.get('ai_visibility', 0)}
            </td>

            <td>
                {competitor.get('geo_score', 0)}
            </td>

            <td>
                {competitor.get('content_depth', '')}
            </td>

            <td>
                {competitor.get('word_count', 0)}
            </td>

        </tr>
        """

    # =====================================
    # HTML
    # =====================================

    html = f"""

    <html>

    <head>

    <style>

    body {{

        font-family: Arial;

        background:#F5F7FB;

        padding:40px;

        color:#111827;

        line-height:1.7;
    }}

    .hero {{

        margin-bottom:50px;
    }}

    .hero-title {{

        font-size:56px;

        font-weight:700;
    }}

    .hero-subtitle {{

        font-size:20px;

        color:#6B7280;
    }}

    .metric-grid {{

        display:grid;

        grid-template-columns:
            repeat(4,1fr);

        gap:20px;

        margin-bottom:50px;
    }}

    .metric-card {{

        background:white;

        border-radius:22px;

        padding:30px;

        border:1px solid #E5E7EB;
    }}

    .metric-title {{

        color:#6B7280;

        margin-bottom:12px;
    }}

    .metric-value {{

        font-size:46px;

        font-weight:700;

        margin-bottom:18px;
    }}

    .section {{

        background:white;

        border-radius:24px;

        padding:36px;

        margin-bottom:35px;

        border:1px solid #E5E7EB;
    }}

    .section-title {{

        font-size:32px;

        font-weight:700;

        margin-bottom:26px;
    }}

    .score-bar-bg {{

        width:100%;

        height:10px;

        background:#E5E7EB;

        border-radius:999px;
    }}

    .score-bar-fill {{

        height:10px;

        border-radius:999px;
    }}

    .audit-card {{

        border:1px solid #E5E7EB;

        border-radius:18px;

        padding:24px;

        margin-bottom:24px;
    }}

    .audit-top {{

        display:flex;

        align-items:center;

        gap:14px;

        margin-bottom:18px;
    }}

    .pill {{

        color:white;

        padding:6px 14px;

        border-radius:999px;

        font-size:12px;

        font-weight:700;
    }}

    .leader-pill {{

        background:#111827;

        color:white;

        padding:4px 10px;

        border-radius:999px;

        font-size:11px;

        margin-left:8px;
    }}

    .audit-category {{

        color:#6B7280;
    }}

    .audit-title {{

        font-size:24px;

        font-weight:700;

        margin-bottom:14px;
    }}

    .audit-details {{

        margin-bottom:18px;
    }}

    .audit-recommendation {{

        background:#F9FAFB;

        padding:16px;

        border-radius:12px;
    }}

    .geo-card {{

        border:1px solid #E5E7EB;

        border-radius:18px;

        padding:24px;

        margin-bottom:20px;
    }}

    .geo-top {{

        display:flex;

        align-items:center;

        gap:14px;

        margin-bottom:14px;
    }}

    table {{

        width:100%;

        border-collapse:collapse;
    }}

    th, td {{

        padding:18px;

        border-bottom:1px solid #E5E7EB;

        text-align:left;
    }}

    th {{

        background:#F9FAFB;
    }}

    </style>

    </head>

    <body>

    <div class="hero">

        <div class="hero-title">
            AI Visibility OS
        </div>

        <div class="hero-subtitle">
            Executive AI Visibility Intelligence Report
        </div>

    </div>

    <div class="metric-grid">

        <div class="metric-card">

            <div class="metric-title">
                SEO Maturity
            </div>

            <div class="metric-value">
                {scores.get('seo_score', 0)}
            </div>

            {build_score_bar(
                scores.get('seo_score', 0)
            )}

        </div>

        <div class="metric-card">

            <div class="metric-title">
                AI Visibility
            </div>

            <div class="metric-value">
                {scores.get('ai_visibility_score', 0)}
            </div>

            {build_score_bar(
                scores.get(
                    'ai_visibility_score',
                    0
                )
            )}

        </div>

        <div class="metric-card">

            <div class="metric-title">
                GEO / AEO
            </div>

            <div class="metric-value">
                {scores.get('geo_score', 0)}
            </div>

            {build_score_bar(
                scores.get('geo_score', 0)
            )}

        </div>

        <div class="metric-card">

            <div class="metric-title">
                Competitive Readiness
            </div>

            <div class="metric-value">
                {scores.get(
                    'competitive_readiness',
                    0
                )}
            </div>

            {build_score_bar(
                scores.get(
                    'competitive_readiness',
                    0
                )
            )}

        </div>

    </div>

    <div class="section">

        <div class="section-title">
            Executive Intelligence Summary
        </div>

        <p>
            {executive_summary}
        </p>

    </div>

    <div class="section">

        <div class="section-title">
            Competitive Benchmarking
        </div>

        <table>

            <tr>

                <th>Competitor</th>

                <th>SEO</th>

                <th>AI Visibility</th>

                <th>GEO/AEO</th>

                <th>Content Depth</th>

                <th>Words</th>

            </tr>

            {competitor_html}

        </table>

    </div>

    <div class="section">

        <div class="section-title">
            Technical SEO Audit
        </div>

        {audit_html}

    </div>

    <div class="section">

        <div class="section-title">
            GEO / AEO Intelligence
        </div>

        {geo_html}

    </div>

    <div class="section">

        <div class="section-title">
            SERP Visibility Intelligence
        </div>

        <p>
            {serp_analysis}
        </p>

    </div>

    <div class="section">

        <div class="section-title">
            Strategic Recommendations
        </div>

        <p>
            {recommendations}
        </p>

    </div>

    </body>

    </html>
    """

    return html