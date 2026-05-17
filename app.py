import time
import streamlit as st

from tools.orchestrator import (
    run_ai_strategy
)

from tools.html_report_renderer import (
    render_html_report
)


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(

    page_title="AI Visibility OS",

    page_icon="🧠",

    layout="wide",

    initial_sidebar_state="expanded"
)


# =========================================
# SESSION STATE
# =========================================

if "messages" not in st.session_state:

    st.session_state.messages = []

if "report" not in st.session_state:

    st.session_state.report = None


# =========================================
# CLEAN MODERN CSS
# =========================================

st.markdown(

    """

    <style>

    /* ====================================
       GLOBAL
    ==================================== */

    .stApp {

        background-color: #F5F7FB;

        color: #111827;
    }

    /* ====================================
       SIDEBAR
    ==================================== */

    section[data-testid="stSidebar"] {

        background-color: #FFFFFF;

        border-right: 1px solid #E5E7EB;
    }

    section[data-testid="stSidebar"] * {

        color: #111827 !important;
    }

    /* ====================================
       USER MESSAGE
    ==================================== */

    .user-bubble {

        background-color: #4F46E5;

        color: white;

        padding: 14px 18px;

        border-radius: 18px;

        margin-top: 18px;

        margin-bottom: 14px;

        width: fit-content;

        max-width: 75%;

        margin-left: auto;

        font-size: 15px;

        box-shadow:
            0 2px 8px rgba(79,70,229,0.12);
    }

    /* ====================================
       EXECUTION BOX
    ==================================== */

    .execution-box {

        background-color: white;

        border: 1px solid #E5E7EB;

        border-radius: 16px;

        padding: 18px;

        margin-top: 20px;

        margin-bottom: 20px;

        color: #374151;

        font-size: 15px;
    }

    /* ====================================
       METRIC CARDS
    ==================================== */

    div[data-testid="metric-container"] {

        background-color: white;

        border: 1px solid #E5E7EB;

        padding: 18px;

        border-radius: 16px;
    }

    /* ====================================
       CHAT INPUT
    ==================================== */

    .stChatInputContainer {

        background-color: #F5F7FB;
    }

    textarea {

        background-color: white !important;

        border: 1px solid #E5E7EB !important;

        color: #111827 !important;

        border-radius: 16px !important;
    }

    /* ====================================
       BUTTONS
    ==================================== */

    .stButton button {

        background-color: #4F46E5;

        color: white;

        border-radius: 12px;

        border: none;
    }

    /* ====================================
       SCROLLBAR
    ==================================== */

    ::-webkit-scrollbar {

        width: 10px;
    }

    ::-webkit-scrollbar-track {

        background: #F3F4F6;
    }

    ::-webkit-scrollbar-thumb {

        background: #D1D5DB;

        border-radius: 20px;
    }

    </style>

    """,

    unsafe_allow_html=True
)


# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("🧠 AI Visibility OS")

    st.caption(
        "Autonomous orchestration intelligence"
    )

    st.divider()

    st.markdown("### Active Capabilities")

    st.markdown(

        """
        - SEO Intelligence
        - GEO/AEO Analysis
        - AI Visibility Scoring
        - Competitive Analysis
        - Autonomous Recommendations
        - Persistent Intelligence
        """
    )

    st.divider()

    st.markdown("### Runtime Status")

    st.success(
        "AI Runtime Active"
    )

    st.info(
        "Persistent Memory Enabled"
    )


# =========================================
# MAIN HEADER
# =========================================

st.title("🧠 AI Visibility OS")

st.caption(
    "Conversational Autonomous Orchestration Intelligence"
)

st.write("")


# =========================================
# CHAT HISTORY
# =========================================

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(

            f"""
            <div class="user-bubble">
            {message['content']}
            </div>
            """,

            unsafe_allow_html=True
        )

    else:

        with st.container():

            st.write(message["content"])


# =========================================
# CHAT INPUT
# =========================================

prompt = st.chat_input(

    "Analyze a website for AI visibility intelligence..."
)


# =========================================
# EXECUTION
# =========================================

if prompt:

    # =====================================
    # SAVE USER MESSAGE
    # =====================================

    st.session_state.messages.append({

        "role": "user",

        "content": prompt
    })

    st.markdown(

        f"""
        <div class="user-bubble">
        {prompt}
        </div>
        """,

        unsafe_allow_html=True
    )

    # =====================================
    # URL EXTRACTION
    # =====================================

    website_url = "https://example.com"

    words = prompt.split()

    for word in words:

        if (
            "http" in word
            or
            ".com" in word
        ):

            website_url = word

            break

    # =====================================
    # LIVE EXECUTION FEED
    # =====================================

    execution_placeholder = st.empty()

    execution_logs = [

        "🧠 Initializing orchestration runtime...",

        "🔍 Evaluating technical SEO signals...",

        "🌐 Running GEO/AEO intelligence analysis...",

        "📊 Analyzing competitive positioning...",

        "⚡ Expanding orchestration workflows...",

        "📈 Generating intelligence report..."
    ]

    live_html = ""

    for log in execution_logs:

        live_html += f"<p>{log}</p>"

        execution_placeholder.markdown(

            f"""
            <div class="execution-box">
            {live_html}
            </div>
            """,

            unsafe_allow_html=True
        )

        time.sleep(0.5)

    # =====================================
    # RUN ANALYSIS
    # =====================================

    with st.spinner(

        "Executing orchestration intelligence..."
    ):

        try:

            report = run_ai_strategy(

                website_url,

                prompt
            )

            st.session_state.report = report

            orchestration_score = (

                report[
                    "orchestration_metrics"
                ][
                    "orchestration_score"
                ]
            )

            scores = report["scores"]

            # =============================
            # METRICS
            # =============================

            st.write("")

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "SEO",
                    scores["seo_score"]
                )

            with col2:

                st.metric(
                    "AI Visibility",
                    scores[
                        "ai_visibility_score"
                    ]
                )

            with col3:

                st.metric(
                    "Competitive",
                    scores[
                        "competitive_readiness"
                    ]
                )

            with col4:

                st.metric(
                    "Orchestration",
                    orchestration_score
                )

            st.write("")

            # =============================
            # EXEC SUMMARY
            # =============================

            st.subheader(
                "Executive Intelligence Summary"
            )

            st.write(
                report["executive_summary"]
            )

            st.write("")

            # =============================
            # FULL REPORT
            # =============================

            html_report = (
                render_html_report(
                    report
                )
            )

            with st.expander(
                "Open Full Intelligence Report"
            ):

                st.components.v1.html(

                    html_report,

                    height=5000,

                    scrolling=True
                )

            # =============================
            # DOWNLOAD
            # =============================

            st.download_button(

                label="Download Full HTML Report",

                data=html_report,

                file_name="ai_visibility_report.html",

                mime="text/html"
            )

            # =============================
            # SAVE ASSISTANT MESSAGE
            # =============================

            st.session_state.messages.append({

                "role": "assistant",

                "content": (
                    "Autonomous orchestration completed successfully."
                )
            })

        except Exception as error:

            st.error(
                f"Execution Error: {error}"
            )

            st.exception(error)