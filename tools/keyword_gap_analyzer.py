from rake_nltk import Rake
from tools.crawler import crawl_website

import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

def analyze_keyword_gap(main_url, competitor_url):

    main = crawl_website(main_url)

    competitor = crawl_website(competitor_url)

    rake = Rake()

    # ====================================
    # EXTRACT MAIN PAGE KEYWORDS
    # ====================================

    main_text = (
        main["title"] + " " +
        main["description"]
    )

    rake.extract_keywords_from_text(main_text)

    main_keywords = rake.get_ranked_phrases()[:15]

    # ====================================
    # EXTRACT COMPETITOR KEYWORDS
    # ====================================

    competitor_text = (
        competitor["title"] + " " +
        competitor["description"]
    )

    rake.extract_keywords_from_text(
        competitor_text
    )

    competitor_keywords = (
        rake.get_ranked_phrases()[:15]
    )

    # ====================================
    # GAP ANALYSIS
    # ====================================

    gaps = []

    for keyword in competitor_keywords:

        if keyword not in main_keywords:

            gaps.append(keyword)

    # ====================================
    # STRATEGIC INSIGHTS
    # ====================================

    insights = []

    if len(gaps) > 0:

        insights.append(
            "Competitor ranks with semantic keyword coverage not strongly represented on the target website."
        )

    if competitor["word_count"] > main["word_count"]:

        insights.append(
            "Competitor content depth may support broader long-tail keyword ownership."
        )

    if competitor["geo_score"] > main["geo_score"]:

        insights.append(
            "Competitor appears more optimized for AI-search and answer-engine visibility."
        )

    # ====================================
    # PRIORITY ACTIONS
    # ====================================

    actions = []

    if len(gaps) > 0:

        actions.append(
            "Expand semantic keyword coverage using competitor keyword themes."
        )

    actions.append(
        "Create structured technical content targeting high-intent engineering and commercial search terms."
    )

    return {

        "main_keywords": main_keywords,

        "competitor_keywords": competitor_keywords,

        "keyword_gaps": gaps,

        "insights": insights,

        "actions": actions
    }