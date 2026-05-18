import json


# =========================================
# SCHEMA EXTRACTION
# =========================================

def extract_schema(soup):

    schemas = []

    scripts = soup.find_all(

        "script",

        attrs={
            "type":
            "application/ld+json"
        }
    )

    for script in scripts:

        try:

            data = json.loads(
                script.string
            )

            if isinstance(data, dict):

                schema_type = data.get(
                    "@type"
                )

                if schema_type:

                    schemas.append(
                        schema_type
                    )

        except:

            pass

    return {

        "schemas": schemas,

        "schema_found":
            len(schemas) > 0
    }