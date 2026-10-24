import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Kuvera Mutual Fund FAQ Assistant",
    page_icon="📊",
    layout="centered"
)

# Persistent Disclaimer & Welcome Banner
st.markdown("### 📊 Kuvera Mutual Fund FAQ Assistant")
st.info("⚠️ **Facts-only. No investment advice.** Last updated from sources: October 2026.")
st.write("Welcome! Ask factual questions about Mirae Asset mutual fund schemes (Expense ratio, Exit load, Minimum SIP, ELSS Lock-in, Riskometer, Benchmark) or statement downloads.")

# Knowledge Base (Curated Factual Corpus)
KNOWLEDGE_BASE = {
    "expense ratio": {
        "answer": "The Total Expense Ratio (TER) varies by plan (Direct vs. Regular) and is updated periodically in accordance with SEBI limits based on daily net assets. You can view the exact daily updated slab-wise expense ratios directly on the official disclosure portal.",
        "link": "https://www.miraeassetmf.co.in/statutory-disclosure/total-expense-ratio",
        "source_title": "Mirae Asset TER Disclosures"
    },
    "exit load": {
        "answer": "For Mirae Asset schemes, an exit load may be levied if units are redeemed or switched out within a specified timeframe from the date of allotment, as detailed in the scheme document. Please refer to the latest Scheme Information Document (SID) or monthly factsheet for exact percentage slabs.",
        "link": "https://www.miraeassetmf.co.in/downloads/scheme-information-document",
        "source_title": "Mirae Asset Scheme Information Documents"
    },
    "minimum sip": {
        "answer": "The minimum SIP investment amount for Mirae Asset schemes is typically ₹500 with daily, weekly, monthly, or quarterly frequency options. Kindly review the Fund KIM for any recent transaction limit revisions.",
        "link": "https://www.miraeassetmf.co.in/downloads/key-information-memorandum",
        "source_title": "Mirae Asset KIM & Application Form"
    },
    "elss lock-in": {
        "answer": "Mirae Asset Tax Saver Fund is an Equity Linked Saving Scheme (ELSS) which carries a mandatory statutory lock-in period of 3 years from the date of unit allotment under Section 80C. No redemptions or switches are permitted during this lock-in window.",
        "link": "https://www.miraeassetmf.co.in/mutual-fund/equity/mirae-asset-tax-saver-fund",
        "source_title": "Mirae Asset Tax Saver Fund Overview"
    },
    "riskometer": {
        "answer": "Scheme riskometers and benchmarks (such as NIFTY LargeCap 100 TRI or NIFTY India Consumption TRI) are evaluated and updated monthly in the official factsheet based on portfolio asset composition.",
        "link": "https://www.miraeassetmf.co.in/downloads/factsheet",
        "source_title": "Mirae Asset Monthly Factsheet"
    },
    "statement": {
        "answer": "You can download your capital-gains or account statements on Kuvera by navigating to your Profile section, selecting Documents, and choosing Capital Gains to generate and download the report for your chosen financial year. No PII is stored or processed by this assistant.",
        "link": "https://support.kuvera.in/support/solutions/",
        "source_title": "Kuvera Support Center"
    }
}

# Example Query Buttons for Easy Interaction
st.write("**Quick-Click Example Questions:**")
col1, col2, col3 = st.columns(3)

selected_query = None
if col1.button("Expense Ratio?"):
    selected_query = "expense ratio"
if col2.button("ELSS Lock-in?"):
    selected_query = "elss lock-in"
if col3.button("Capital Gains Statement?"):
    selected_query = "statement"

# User Text Input
user_query = st.text_input("Or type your question here:", value=selected_query if selected_query else "")

# Response Generation Logic
if user_query:
    query_lower = user_query.lower()
    
    # Check for advice or portfolio opinions (Guardrail Refusal)
    advice_keywords = ["should i buy", "should i sell", "best fund", "recommend", "invest in", "good return"]
    if any(keyword in query_lower for keyword in advice_keywords):
        st.warning("I provide factual scheme details only and cannot offer investment advice. Please consult a SEBI-registered advisor or check official scheme documents.")
        st.markdown("[🔗 Visit Official Scheme Disclosures](https://www.miraeassetmf.co.in/downloads/scheme-information-document)")
    else:
        # Match against knowledge base keywords
        matched = False
        for key, data in KNOWLEDGE_BASE.items():
            if key in query_lower:
                matched = True
                st.success(data["answer"])
                st.markdown(f"**Source:** [{data['source_title']}]({data['link']})")
                st.caption("Last updated from sources: October 2026")
                break
        
        if not matched:
            st.info("I can answer facts regarding expense ratios, exit loads, minimum SIP, ELSS lock-ins, riskometers, benchmarks, and statement downloads for Mirae Asset schemes on Kuvera. Please try asking about one of these topics.")