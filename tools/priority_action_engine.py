# =========================================
# PRIORITY ACTION ENGINE
# =========================================

def build_priority_actions(site_data):

    actions = []

    # =====================================
    # SAFE GETTERS
    # =====================================

    seo_score = site_data.get(
        "seo_score",
        50
    )

    geo_score = site_data.get(
        "geo_score",
        50
    )

    missing_alt = site_data.get(
        "missing_alt",
        0
    )

    missing_h1 = site_data.get(
        "missing_h1",
        0
    )

    schema_found = site_data.get(
        "schema_found",
        False
    )

    word_count = site_data.get(
        "word_count",
        0
    )

    # =====================================
    # SEO SCORE
    # =====================================

    if seo_score < 70:

        actions.append({

            "priority":
                "High",

            "action":
                (
                    "Improve technical SEO "
                    "optimization and metadata "
                    "structure."
                )
        })

    # =====================================
    # GEO SCORE
    # =====================================

    if geo_score < 70:

        actions.append({

            "priority":
                "Critical",

            "action":
                (
                    "Improve AI discoverability "
                    "and GEO optimization."
                )
        })

    # =====================================
    # ALT TAGS
    # =====================================

    if missing_alt > 0:

        actions.append({

            "priority":
                "Medium",

            "action":
                (
                    "Add missing image alt "
                    "attributes for accessibility "
                    "and semantic optimization."
                )
        })

    # =====================================
    # H1 TAGS
    # =====================================

    if missing_h1 > 0:

        actions.append({

            "priority":
                "Medium",

            "action":
                (
                    "Improve heading hierarchy "
                    "and H1 optimization."
                )
        })

    # =====================================
    # SCHEMA
    # =====================================

    if not schema_found:

        actions.append({

            "priority":
                "High",

            "action":
                (
                    "Implement structured schema "
                    "markup for AI-search visibility."
                )
        })

    # =====================================
    # CONTENT DEPTH
    # =====================================

    if word_count < 1000:

        actions.append({

            "priority":
                "Medium",

            "action":
                (
                    "Expand topical authority "
                    "through deeper content coverage."
                )
        })

    # =====================================
    # FALLBACK
    # =====================================

    if not actions:

        actions.append({

            "priority":
                "Low",

            "action":
                (
                    "Maintain current optimization "
                    "trajectory and monitor AI visibility."
                )
        })

    return actions