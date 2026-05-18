# =========================================
# HTML REPORT RENDERER
# =========================================

def render_html_report(

    report
):

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

    orchestration_history = report.get(
        "orchestration_history",
        []
    )

    recommendations = report.get(
        "recommendations",
        ""
    )

    # =====================================
    # TECHNICAL AUDIT HTML
    # =====================================

    audit_html = ""

    for finding in technical_audit:

        if isinstance(finding, dict):

            audit_html += f"""

            <div class="audit-card">

                <h3>
                    {finding.get('priority', 'Medium')}
                    — {finding.get('category', 'Audit')}
                </h3>

                <p>
                    <strong>Issue:</strong>
                    {finding.get('issue', '')}
                </p>

                <p>
                    <strong>Details:</strong>
                    {finding.get('details', '')}
                </p>

                <p>
                    <strong>Recommendation:</strong>
                    {finding.get('recommendation', '')}
                </p>

            </div>
            """

        else:

            audit_html += f"""

            <div class="audit-card">

                <p>{finding}</p>

            </div>
            """

    # =====================================
    # ORCHESTRATION HTML
    # =====================================

    orchestration_html = ""

    for item in orchestration_history:

        orchestration_html += f"""

        <li>{item}</li>

        """

    # =====================================
    # FINAL HTML
    # =====================================

    html = f"""

    <html>

    <head>

    <style>

    body {{

        font-family: Arial, sans-serif;

        background-color: #F5F7FB;

        color: #111827;

        padding: 40px;
    }}

    .hero {{

        margin-bottom: 40px;
    }}

    .title {{

        font-size: 48px;

        font-weight: bold;

        margin-bottom: 10px;
    }}

    .subtitle {{

        color: #6B7280;

        font-size: 18px;
    }}

    .section {{

        background: white;

        padding: 30px;

        border-radius: 16px;

        margin-bottom: 30px;

        border: 1px solid #E5E7EB;
    }}

    .metric-grid {{

        display: grid;

        grid-template-columns: repeat(4, 1fr);

        gap: 20px;

        margin-bottom: 40px;
    }}

    .metric-card {{

        background: white;

        padding: 20px;

        border-radius: 16px;

        border: 1px solid #E5E7EB;
    }}

    .metric-title {{

        color: #6B7280;

        margin-bottom: 10px;
    }}

    .metric-value {{

        font-size: 32px;

        font-weight: bold;
    }}

    .audit-card {{

        border: 1px solid #E5E7EB;

        padding: 20px;

        border-radius: 12px;

        margin-bottom: 20px;
    }}

    </style>

    </head>

    <body>

    <div class="hero">

        <div class="title">
            AI Visibility OS
        </div>

        <div class="subtitle">
            Autonomous AI Visibility Intelligence Report
        </div>

    </div>

    <div class="metric-grid">

        <div class="metric-card">

            <div class="metric-title">
                SEO Score
            </div>

            <div class="metric-value">
                {scores.get('seo_score', 0)}
            </div>

        </div>

        <div class="metric-card">

            <div class="metric-title">
                AI Visibility
            </div>

            <div class="metric-value">
                {scores.get('ai_visibility_score', 0)}
            </div>

        </div>

        <div class="metric-card">

            <div class="metric-title">
                GEO Score
            </div>

            <div class="metric-value">
                {scores.get('geo_score', 0)}
            </div>

        </div>

        <div class="metric-card">

            <div class="metric-title">
                Competitive Readiness
            </div>

            <div class="metric-value">
                {scores.get('competitive_readiness', 0)}
            </div>

        </div>

    </div>

    <div class="section">

        <h2>
            Executive Intelligence Summary
        </h2>

        <p>
            {executive_summary}
        </p>

    </div>

    <div class="section">

        <h2>
            Technical SEO Audit
        </h2>

        {audit_html}

    </div>

    <div class="section">

        <h2>
            Orchestration Runtime
        </h2>

        <ul>

            {orchestration_html}

        </ul>

    </div>

    <div class="section">

        <h2>
            Strategic Recommendations
        </h2>

        <p>
            {recommendations}
        </p>

    </div>

    </body>

    </html>
    """

    return html