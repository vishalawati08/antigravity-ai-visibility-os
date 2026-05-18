import matplotlib.pyplot as plt


# =========================================
# SCORE CHART
# =========================================

def generate_score_chart(

    scores,

    output_path="score_chart.png"
):

    labels = [

        "SEO",

        "AI Visibility",

        "GEO/AEO",

        "Competitive"
    ]

    values = [

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

    plt.figure(
        figsize=(8, 5)
    )

    bars = plt.bar(

        labels,

        values
    )

    plt.ylim(0, 100)

    plt.ylabel(
        "Score"
    )

    plt.title(
        "AI Visibility Intelligence Scores"
    )

    # =====================================
    # LABELS
    # =====================================

    for bar in bars:

        height = bar.get_height()

        plt.text(

            bar.get_x()
            + bar.get_width() / 2,

            height + 2,

            str(int(height)),

            ha="center"
        )

    plt.tight_layout()

    plt.savefig(
        output_path
    )

    plt.close()

    return output_path


# =========================================
# COMPETITOR CHART
# =========================================

def generate_competitor_chart(

    competitors,

    output_path="competitor_chart.png"
):

    names = []

    seo_scores = []

    for competitor in competitors:

        names.append(

            competitor.get(
                "name",
                "Unknown"
            )
        )

        seo_scores.append(

            competitor.get(
                "seo_score",
                0
            )
        )

    plt.figure(
        figsize=(10, 5)
    )

    bars = plt.bar(

        names,

        seo_scores
    )

    plt.ylim(0, 100)

    plt.ylabel(
        "SEO Score"
    )

    plt.title(
        "Competitive Benchmarking"
    )

    # =====================================
    # LABELS
    # =====================================

    for bar in bars:

        height = bar.get_height()

        plt.text(

            bar.get_x()
            + bar.get_width() / 2,

            height + 2,

            str(int(height)),

            ha="center"
        )

    plt.tight_layout()

    plt.savefig(
        output_path
    )

    plt.close()

    return output_path