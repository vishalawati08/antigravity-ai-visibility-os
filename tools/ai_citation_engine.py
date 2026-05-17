# =========================================
# AI CITATION READINESS ENGINE
# =========================================

def analyze_ai_citation_readiness(site_data):

    findings = []

    score = 50

    # =====================================
    # WORD COUNT
    # =====================================

    if site_data["word_count"] > 1200:

        findings.append(
            "Strong semantic content depth "
            "supports AI summarization."
        )

        score += 10

    else:

        findings.append(
            "Limited semantic depth weakens "
            "AI-answer extraction quality."
        )

    # =====================================
    # H1 STRUCTURE
    # =====================================

    if len(site_data["h1_tags"]) == 1:

        findings.append(
            "Clean heading hierarchy improves "
            "AI parsing clarity."
        )

        score += 10

    else:

        findings.append(
            "Fragmented heading structure may "
            "reduce semantic interpretability."
        )

    # =====================================
    # SCHEMA
    # =====================================

    if site_data["schema_found"]:

        findings.append(
            "Structured schema markup improves "
            "AI-citation eligibility."
        )

        score += 15

    else:

        findings.append(
            "Missing schema reduces AI "
            "knowledge extraction potential."
        )

    # =====================================
    # IMAGE ALT
    # =====================================

    if site_data["missing_alt"] == 0:

        findings.append(
            "Strong multimodal accessibility "
            "supports AI-search visibility."
        )

        score += 5

    else:

        findings.append(
            "Missing ALT attributes reduce "
            "multimodal AI discoverability."
        )

    # =====================================
    # CONTENT QUALITY
    # =====================================

    if site_data["word_count"] < 700:

        findings.append(
            "Content architecture appears "
            "too shallow for strong AI citation."
        )

    # =====================================
    # FINAL SCORE
    # =====================================

    if score > 100:

        score = 100

    return {

        "citation_score":
            score,

        "findings":
            findings
    }