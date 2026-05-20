import streamlit as st

from tools.orchestrator import (
    run_ai_strategy
)

from tools.html_report_renderer import (
    render_html_report
)

from tools.pdf_exporter import (
    export_pdf
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Visibility OS",
    layout="wide"
)


# =========================================
# SESSION STATE
# =========================================

if "report" not in st.session_state:

    st.session_state.report = None

if "html_report" not in st.session_state:

    st.session_state.html_report = None


# =========================================
# CUSTOM CSS
# =========================================

st.markdown(
    """
    <style>

    .main {
        background-color: #F5F7FB;
    }

    .hero {
        padding-top: 20px;
        padding-bottom: 30px;
    }

    .hero-title {
        font-size: 58px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #6B7280;
        max-width: 900px;
    }

    .input-card {
        background: white;
        padding: 30px;
        border-radius: 22px;
        border: 1px solid #E5E7EB;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================
# HERO SECTION
# =========================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            AI Visibility OS
        </div>

        <div class="hero-subtitle">
            Enterprise-grade AI Visibility,
            SEO and GEO/AEO Intelligence Platform.
            Analyze websites, benchmark competitors,
            identify semantic gaps and generate
            executive intelligence reports.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# INPUT SECTION
# =========================================

st.markdown(
    "<div class='input-card'>",
    unsafe_allow_html=True
)

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

prompt = st.text_area(
    "Audit Objective",
    placeholder="Example: Analyze AI visibility, SEO maturity, GEO/AEO readiness and competitor benchmarking.",
    height=140
)

run_button = st.button(
    "Generate Executive Intelligence Report",
    use_container_width=True
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# =========================================
# RUN ANALYSIS
# =========================================

if run_button:

    if not url:

        st.error(
            "Please enter a website URL."
        )

    else:

        if not prompt:

            prompt = (
                "Analyze SEO maturity, AI visibility, "
                "GEO/AEO readiness and competitive positioning."
            )

        with st.spinner(
            "Running AI Visibility Intelligence Analysis..."
        ):

            try:

                report = run_ai_strategy(
                    url,
                    prompt
                )

                html_report = render_html_report(
                    report
                )

                st.session_state.report = report

                st.session_state.html_report = html_report

            except Exception as error:

                st.error(
                    f"Analysis failed: {str(error)}"
                )


# =========================================
# REPORT DISPLAY
# =========================================

if st.session_state.html_report:

    st.html(
        st.session_state.html_report
    )


# =========================================
# PDF EXPORT
# =========================================

if st.session_state.report:

    try:

        pdf_path = export_pdf(
            st.session_state.report
        )

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="Download Executive PDF Report",
                data=pdf_file,
                file_name="ai_visibility_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    except Exception as error:

        st.warning(
            f"PDF export failed: {str(error)}"
        )