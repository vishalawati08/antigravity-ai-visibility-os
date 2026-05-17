from tools.crawler import crawl_website


def compare_websites(main_url, competitor_url):

    main = crawl_website(main_url)

    competitor = crawl_website(competitor_url)

    findings = []

    # =========================
    # WORD COUNT
    # =========================

    if competitor["word_count"] > main["word_count"]:

        findings.append(
            f"Competitor content depth is stronger ({competitor['word_count']} words vs {main['word_count']}), improving topical authority."
        )

    else:

        findings.append(
            "Your website demonstrates stronger content depth than the competitor."
        )

    # =========================
    # GEO SCORE
    # =========================

    if competitor["geo_score"] > main["geo_score"]:

        findings.append(
            "Competitor demonstrates stronger AI-search readiness and GEO optimization signals."
        )

    else:

        findings.append(
            "Your website currently demonstrates stronger AI-search optimization signals."
        )

    # =========================
    # SCHEMA
    # =========================

    if competitor["schema_found"] > main["schema_found"]:

        findings.append(
            "Competitor uses more structured schema markup, improving machine-readable visibility."
        )

    # =========================
    # ANSWER BLOCKS
    # =========================

    if competitor["answer_blocks"] > main["answer_blocks"]:

        findings.append(
            "Competitor content appears more optimized for AI-generated answer extraction."
        )

    # =========================
    # H1 STRUCTURE
    # =========================

    if len(main["h1_tags"]) > len(competitor["h1_tags"]):

        findings.append(
            "Multiple H1 tags on the target page may weaken semantic clarity compared to competitor structure."
        )

    # =========================
    # SEO SCORE
    # =========================

    if competitor["seo_score"] > main["seo_score"]:

        findings.append(
            f"Competitor maintains stronger overall SEO health ({competitor['seo_score']}/100 vs {main['seo_score']}/100)."
        )

    else:

        findings.append(
            "Your website currently maintains stronger overall SEO health than the competitor."
        )

    return {
        "main_site": main,
        "competitor_site": competitor,
        "findings": findings
    }