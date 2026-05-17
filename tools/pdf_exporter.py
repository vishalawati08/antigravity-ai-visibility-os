from weasyprint import HTML


# =========================================
# PDF EXPORTER
# =========================================

def export_pdf(html_report):

    output_path = "AI_Visibility_Report.pdf"

    HTML(
        string=html_report
    ).write_pdf(output_path)

    return output_path