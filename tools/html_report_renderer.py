from datetime import datetime


def render_html_report(report):

    timestamp = datetime.now().strftime(
        "%d %B %Y | %I:%M %p"
    )

    total_runs = len(
        report["orchestration_history"]
    )

    orchestration_score = (
        report["orchestration_metrics"][
            "orchestration_score"
        ]
    )

    html = f"""

    <html>

    <head>

    <style>

    body {{
        background-color: #0A0F1C;
        color: #E5E7EB;
        font-family: Arial, sans-serif;
        padding: 50px;
        line-height: 1.8;
    }}

    .container {{
        max-width: 1200px;
        margin: auto;
    }}

    .hero {{
        margin-bottom: 60px;
        padding-bottom: 30px;
        border-bottom: 1px solid #1F2937;
    }}

    .hero-title {{
        font-size: 58px;
        font-weight: bold;
        color: #60A5FA;
    }}

    .hero-subtitle {{
        color: #94A3B8;
        font-size: 20px;
        margin-top: 10px;
    }}

    .hero-meta {{
        color: #64748B;
        font-size: 14px;
        margin-top: 10px;
    }}

    .score-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin-top: 40px;
        margin-bottom: 60px;
    }}

    .score-card {{
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
    }}

    .score-number {{
        font-size: 42px;
        font-weight: bold;
        color: #60A5FA;
    }}

    .score-label {{
        margin-top: 12px;
        color: #94A3B8;
    }}

    .section {{
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 40px;
    }}

    .section-title {{
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 20px;
    }}

    .section-content {{
        font-size: 18px;
        color: #D1D5DB;
    }}

    ul {{
        margin-top: 20px;
    }}

    li {{
        margin-bottom: 12px;
    }}

    .footer {{
        text-align: center;
        margin-top: 80px;
        color: #64748B;
    }}

    </style>

    </head>

    <body>

    <div class="container">

        <!-- HERO -->

        <div class="hero">

            <div class="hero-title">
                AI Visibility OS
            </div>

            <div class="hero-subtitle">
                Autonomous Orchestration Intelligence Report
            </div>

            <div class="hero-meta">
                Generated: {timestamp}
            </div>

            <div class="hero-meta">
                Historical Runs: {total_runs}
            </div>

        </div>

        <!-- SCORE GRID -->

        <div class="score-grid">

            <div class="score-card">

                <div class="score-number">
                    {report["scores"]["seo_score"]}
                </div>

                <div class="score-label">
                    SEO Maturity
                </div>

            </div>

            <div class="score-card">

                <div class="score-number">
                    {report["scores"]["ai_visibility_score"]}
                </div>

                <div class="score-label">
                    AI Visibility
                </div>

            </div>

            <div class="score-card">

                <div class="score-number">
                    {report["scores"]["competitive_readiness"]}
                </div>

                <div class="score-label">
                    Competitive Readiness
                </div>

            </div>

            <div class="score-card">

                <div class="score-number">
                    {orchestration_score}
                </div>

                <div class="score-label">
                    Orchestration Intelligence
                </div>

            </div>

        </div>

        <!-- EXECUTIVE SUMMARY -->

        <div class="section">

            <div class="section-title">
                Executive Summary
            </div>

            <div class="section-content">
                {report["executive_summary"]}
            </div>

        </div>

        <!-- ORCHESTRATION -->

        <div class="section">

            <div class="section-title">
                Autonomous Research Orchestration
            </div>

            <div class="section-content">

                <ul>

                    {
                        "".join(
                            [
                                f"<li>{step}</li>"
                                for step in report[
                                    "orchestration_results"
                                ]["execution_log"]
                            ]
                        )
                    }

                </ul>

            </div>

        </div>

        <!-- REFLECTION -->

        <div class="section">

            <div class="section-title">
                Reflective Orchestration Analysis
            </div>

            <div class="section-content">

                <ul>

                    {
                        "".join(
                            [
                                f"<li><b>{item['issue']}</b>: "
                                f"{item['recommendation']}</li>"
                                for item in report[
                                    "reflections"
                                ]
                            ]
                        )
                    }

                </ul>

            </div>

        </div>

        <!-- AUTONOMOUS TASKS -->

        <div class="section">

            <div class="section-title">
                Autonomous Task Planning
            </div>

            <div class="section-content">

                <ul>

                    {
                        "".join(
                            [
                                f"<li><b>{task['priority']}</b>: "
                                f"{task['task']}</li>"
                                for task in report[
                                    "autonomous_tasks"
                                ]
                            ]
                        )
                    }

                </ul>

            </div>

        </div>

        <!-- AI VISIBILITY -->

        <div class="section">

            <div class="section-title">
                AI Visibility Assessment
            </div>

            <div class="section-content">
                {report["ai_visibility"]}
            </div>

        </div>

        <!-- AI OVERVIEW -->

        <div class="section">

            <div class="section-title">
                AI Overview Simulation
            </div>

            <div class="section-content">
                {report["ai_overview"]}
            </div>

        </div>

        <!-- COMPETITOR -->

        <div class="section">

            <div class="section-title">
                Competitive Positioning
            </div>

            <div class="section-content">
                {report["competitor_analysis"]}
            </div>

            {report["competitor_table"]}

        </div>

        <!-- ACTION MATRIX -->

        <div class="section">

            <div class="section-title">
                Priority Action Matrix
            </div>

            <div class="section-content">
                {report["action_matrix"]}
            </div>

        </div>

        <!-- SERP -->

        <div class="section">

            <div class="section-title">
                SERP Ownership Risks
            </div>

            <div class="section-content">
                {report["serp_analysis"]}
            </div>

        </div>

        <!-- RECOMMENDATIONS -->

        <div class="section">

            <div class="section-title">
                Strategic Recommendations
            </div>

            <div class="section-content">
                {report["recommendations"]}
            </div>

        </div>

        <!-- FOOTER -->

        <div class="footer">

            Generated autonomously by AI Visibility OS

        </div>

    </div>

    </body>

    </html>

    """

    return html