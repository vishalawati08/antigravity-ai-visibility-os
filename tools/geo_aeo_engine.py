# =========================================
# GEO / AEO ANALYSIS ENGINE
# =========================================

def analyze_geo_aeo(

    crawl_data
):

    results = []

    # =====================================
    # FAQ ANALYSIS
    # =====================================

    if crawl_data.get(
        "faq_detected",
        False
    ):

        results.append({

            "category":
                "FAQ Readiness",

            "status":
                "Strong",

            "details":
                "FAQ-style content detected, improving AI-answer discoverability."
        })

    else:

        results.append({

            "category":
                "FAQ Readiness",

            "status":
                "Weak",

            "details":
                "No FAQ structures detected. AI-answer readiness may be limited."
        })

    # =====================================
    # SCHEMA ANALYSIS
    # =====================================

    if crawl_data.get(
        "schema_found",
        False
    ):

        results.append({

            "category":
                "Structured Data",

            "status":
                "Strong",

            "details":
                "Structured data detected, improving machine readability and semantic understanding."
        })

    else:

        results.append({

            "category":
                "Structured Data",

            "status":
                "Weak",

            "details":
                "No structured schema markup detected."
        })

    # =====================================
    # CONTENT DEPTH
    # =====================================

    word_count = crawl_data.get(
        "word_count",
        0
    )

    if word_count > 8000:

        status = "Strong"

    elif word_count > 3000:

        status = "Moderate"

    else:

        status = "Weak"

    results.append({

        "category":
            "Content Depth",

        "status":
            status,

        "details":
            f"Website contains approximately {word_count} analyzed words."
    })

    # =====================================
    # SEMANTIC STRUCTURE
    # =====================================

    h2_count = len(

        crawl_data.get(
            "h2_tags",
            []
        )
    )

    if h2_count >= 10:

        status = "Strong"

    elif h2_count >= 5:

        status = "Moderate"

    else:

        status = "Weak"

    results.append({

        "category":
            "Semantic Structure",

        "status":
            status,

        "details":
            f"{h2_count} semantic H2 structures detected."
    })

    # =====================================
    # AI READINESS
    # =====================================

    results.append({

        "category":
            "AI Readiness",

        "status":
            crawl_data.get(
                "ai_readiness",
                "Low"
            ),

        "details":
            "AI-answer readiness estimated based on semantic architecture and machine-readable content."
    })

    return results