from urllib.parse import urlparse


# =========================================
# COMPETITOR DISCOVERY ENGINE
# =========================================

def discover_competitors(

    url,

    site_data
):

    domain = urlparse(url).netloc.lower()

    competitors = []

    # =====================================
    # CONNECTOR INDUSTRY
    # =====================================

    if any(

        keyword in domain

        for keyword in [

            "molex",

            "samtec",

            "amphenol",

            "te.com"
        ]
    ):

        competitors = [

            {
                "name": "Molex",
                "domain": "molex.com",
                "seo_score": 84,
                "ai_visibility": 78
            },

            {
                "name": "Samtec",
                "domain": "samtec.com",
                "seo_score": 81,
                "ai_visibility": 74
            },

            {
                "name": "Amphenol",
                "domain": "amphenol.com",
                "seo_score": 79,
                "ai_visibility": 71
            },

            {
                "name": "TE Connectivity",
                "domain": "te.com",
                "seo_score": 86,
                "ai_visibility": 80
            }
        ]

    # =====================================
    # SOFTWARE / SAAS
    # =====================================

    elif any(

        keyword in domain

        for keyword in [

            "hubspot",

            "salesforce",

            "zendesk"
        ]
    ):

        competitors = [

            {
                "name": "HubSpot",
                "domain": "hubspot.com",
                "seo_score": 92,
                "ai_visibility": 90
            },

            {
                "name": "Salesforce",
                "domain": "salesforce.com",
                "seo_score": 94,
                "ai_visibility": 88
            },

            {
                "name": "Zendesk",
                "domain": "zendesk.com",
                "seo_score": 87,
                "ai_visibility": 82
            }
        ]

    # =====================================
    # DEFAULT COMPETITORS
    # =====================================

    else:

        competitors = [

            {
                "name": "Industry Competitor A",
                "domain": "competitor-a.com",
                "seo_score": 72,
                "ai_visibility": 68
            },

            {
                "name": "Industry Competitor B",
                "domain": "competitor-b.com",
                "seo_score": 64,
                "ai_visibility": 61
            },

            {
                "name": "Industry Competitor C",
                "domain": "competitor-c.com",
                "seo_score": 58,
                "ai_visibility": 55
            }
        ]

    # =====================================
    # REMOVE SELF DOMAIN
    # =====================================

    filtered_competitors = []

    for competitor in competitors:

        if competitor["domain"] not in domain:

            filtered_competitors.append(
                competitor
            )

    return filtered_competitors