import ollama


def generate_llm_report(site_data, competitors):

    prompt = f"""

You are an elite AI SEO strategist.

Generate a professional executive-style AI visibility audit report.

WEBSITE DATA:
{site_data}

COMPETITOR DATA:
{competitors}

The report must include:

1. Executive Summary
2. AI Visibility Assessment
3. Competitive Positioning
4. SERP Ownership Risks
5. Strategic SEO/GEO Insights
6. AI Search Readiness Analysis
7. Priority Recommendations
8. Executive Conclusion

The writing style must feel:
- strategic
- executive-level
- consulting-grade
- analytical

Avoid generic AI phrasing.
Avoid repetitive writing.

"""

    response = ollama.chat(

        model="llama3",

        messages=[

            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]