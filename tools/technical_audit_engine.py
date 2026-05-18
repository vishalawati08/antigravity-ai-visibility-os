# =========================================
# TECHNICAL AUDIT ENGINE
# =========================================

def generate_technical_audit(

    site_data
):

    findings = []

    # =====================================
    # TITLE TAG
    # =====================================

    if not site_data.get("title"):

        findings.append({

            "priority": "Critical",

            "category": "Metadata",

            "issue": "Missing title tag",

            "details":
                "The page does not contain a title tag.",

            "recommendation":
                "Add a unique SEO-optimized title tag."
        })

    elif len(site_data.get("title", "")) < 30:

        findings.append({

            "priority": "Medium",

            "category": "Metadata",

            "issue": "Short title tag",

            "details":
                "The title tag may be too short for strong search visibility.",

            "recommendation":
                "Expand title tags with primary keyword intent."
        })

    # =====================================
    # META DESCRIPTION
    # =====================================

    if not site_data.get("meta_description"):

        findings.append({

            "priority": "High",

            "category": "Metadata",

            "issue": "Missing meta description",

            "details":
                "Meta descriptions help improve SERP click-through rates.",

            "recommendation":
                "Add compelling meta descriptions for search optimization."
        })

    # =====================================
    # H1 ANALYSIS
    # =====================================

    h1_tags = site_data.get(
        "h1_tags",
        []
    )

    if len(h1_tags) == 0:

        findings.append({

            "priority": "Critical",

            "category": "Structure",

            "issue": "Missing H1 tag",

            "details":
                "No H1 heading was detected on the page.",

            "recommendation":
                "Add a clear keyword-focused H1 heading."
        })

    elif len(h1_tags) > 1:

        findings.append({

            "priority": "Medium",

            "category": "Structure",

            "issue": "Multiple H1 tags detected",

            "details":
                "Multiple H1 tags may dilute semantic clarity.",

            "recommendation":
                "Use a single primary H1 heading."
        })

    # =====================================
    # CONTENT DEPTH
    # =====================================

    word_count = site_data.get(
        "word_count",
        0
    )

    if word_count < 800:

        findings.append({

            "priority": "High",

            "category": "Content",

            "issue": "Thin content detected",

            "details":
                f"Only {word_count} words detected on the page.",

            "recommendation":
                "Expand topical depth and semantic coverage."
        })

    elif word_count > 2500:

        findings.append({

            "priority": "Low",

            "category": "Content",

            "issue": "Strong content depth",

            "details":
                f"{word_count} words detected indicating strong topical coverage.",

            "recommendation":
                "Continue strengthening semantic organization."
        })

    # =====================================
    # SCHEMA
    # =====================================

    if not site_data.get("schema_found"):

        findings.append({

            "priority": "High",

            "category": "Structured Data",

            "issue": "Schema markup missing",

            "details":
                "No structured data was detected.",

            "recommendation":
                "Implement JSON-LD schema markup for better AI discoverability."
        })

    # =====================================
    # FAQ
    # =====================================

    if not site_data.get("faq_detected"):

        findings.append({

            "priority": "Medium",

            "category": "AI Visibility",

            "issue": "FAQ structure not detected",

            "details":
                "FAQ content improves AI answer extraction.",

            "recommendation":
                "Add FAQ-based semantic content blocks."
        })

    # =====================================
    # IMAGE ALT TAGS
    # =====================================

    missing_alt = site_data.get(
        "images_missing_alt",
        0
    )

    if missing_alt > 0:

        findings.append({

            "priority": "Medium",

            "category": "Accessibility",

            "issue": "Images missing ALT attributes",

            "details":
                f"{missing_alt} images are missing ALT text.",

            "recommendation":
                "Add descriptive ALT text to all images."
        })

    # =====================================
    # INTERNAL LINKING
    # =====================================

    internal_links = len(

        site_data.get(
            "internal_links",
            []
        )
    )

    if internal_links < 5:

        findings.append({

            "priority": "Medium",

            "category": "Internal Linking",

            "issue": "Weak internal linking structure",

            "details":
                f"Only {internal_links} internal links detected.",

            "recommendation":
                "Increase contextual internal linking across pages."
        })

    # =====================================
    # CANONICAL
    # =====================================

    if not site_data.get("canonical"):

        findings.append({

            "priority": "Medium",

            "category": "Indexation",

            "issue": "Missing canonical tag",

            "details":
                "Canonical tags help consolidate ranking signals.",

            "recommendation":
                "Add canonical URLs to prevent duplication issues."
        })

    # =====================================
    # AI READINESS
    # =====================================

    ai_readiness = site_data.get(
        "ai_readiness",
        "Low"
    )

    if ai_readiness == "Low":

        findings.append({

            "priority": "High",

            "category": "AI Visibility",

            "issue": "Low AI-search readiness",

            "details":
                "The page lacks strong AI-answer extraction signals.",

            "recommendation":
                "Improve semantic structure, schema and FAQ coverage."
        })

    elif ai_readiness == "High":

        findings.append({

            "priority": "Low",

            "category": "AI Visibility",

            "issue": "Strong AI visibility foundation",

            "details":
                "The page demonstrates good AI-answer readiness.",

            "recommendation":
                "Expand conversational content and entity authority."
        })

    # =====================================
    # NO FINDINGS
    # =====================================

    if len(findings) == 0:

        findings.append({

            "priority": "Low",

            "category": "Technical SEO",

            "issue": "No major technical issues detected",

            "details":
                "The page demonstrates strong technical optimization.",

            "recommendation":
                "Continue monitoring SEO and AI visibility trends."
        })

    return findings