# =========================================
# GEO / AEO INTELLIGENCE ENGINE
# =========================================

def generate_geo_aeo_analysis(

    site_data
):

    findings = []

    # =====================================
    # FAQ ANALYSIS
    # =====================================

    if site_data.get("faq_detected"):

        findings.append({

            "status": "Positive",

            "category": "FAQ Optimization",

            "details":
                "FAQ-style content detected. "
                "This improves AI answer extraction "
                "and conversational discoverability."
        })

    else:

        findings.append({

            "status": "Opportunity",

            "category": "FAQ Optimization",

            "details":
                "No FAQ-focused semantic structure detected. "
                "Adding FAQ content may improve "
                "AI-generated answer visibility."
        })

    # =====================================
    # CONTENT DEPTH
    # =====================================

    word_count = site_data.get(
        "word_count",
        0
    )

    if word_count > 2000:

        findings.append({

            "status": "Positive",

            "category": "Topical Authority",

            "details":
                "Strong content depth detected, "
                "supporting AI-topic understanding."
        })

    elif word_count < 800:

        findings.append({

            "status": "Risk",

            "category": "Topical Authority",

            "details":
                "Thin content may reduce "
                "AI citation potential."
        })

    # =====================================
    # SCHEMA
    # =====================================

    if site_data.get("schema_found"):

        findings.append({

            "status": "Positive",

            "category": "Structured Entities",

            "details":
                "Schema markup detected, improving "
                "machine readability and entity extraction."
        })

    else:

        findings.append({

            "status": "Opportunity",

            "category": "Structured Entities",

            "details":
                "No structured schema detected. "
                "JSON-LD schema improves AI understanding."
        })

    # =====================================
    # HEADINGS
    # =====================================

    h2_count = len(

        site_data.get(
            "h2_tags",
            []
        )
    )

    if h2_count >= 5:

        findings.append({

            "status": "Positive",

            "category": "Semantic Structure",

            "details":
                "Strong heading hierarchy supports "
                "AI semantic parsing."
        })

    else:

        findings.append({

            "status": "Opportunity",

            "category": "Semantic Structure",

            "details":
                "Limited semantic heading structure detected."
        })

    # =====================================
    # AI READINESS
    # =====================================

    ai_readiness = site_data.get(
        "ai_readiness",
        "Low"
    )

    findings.append({

        "status": "Analysis",

        "category": "AI Readiness",

        "details":
            f"Overall AI readiness classified as {ai_readiness}."
    })

    # =====================================
    # ANSWER EXTRACTION
    # =====================================

    paragraphs = site_data.get(
        "paragraphs",
        []
    )

    short_paragraphs = 0

    for para in paragraphs:

        if len(para.split()) < 60:

            short_paragraphs += 1

    if short_paragraphs >= 5:

        findings.append({

            "status": "Positive",

            "category": "Answer Extraction",

            "details":
                "Short-form informational blocks detected. "
                "This may improve AI answer extraction."
        })

    else:

        findings.append({

            "status": "Opportunity",

            "category": "Answer Extraction",

            "details":
                "Consider adding concise answer-focused sections."
        })

    return findings