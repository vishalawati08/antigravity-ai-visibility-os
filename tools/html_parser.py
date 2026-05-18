from bs4 import BeautifulSoup


# =========================================
# PARSE HTML
# =========================================

def parse_html(html):

    soup = BeautifulSoup(

        html,

        "html.parser"
    )

    return soup