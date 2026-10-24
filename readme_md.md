# Kuvera Mutual Fund FAQ Assistant (Facts-Only Prototype)

A lightweight, facts-only FAQ assistant designed to answer factual queries regarding mutual fund schemes (expense ratio, exit load, minimum SIP, ELSS lock-in, riskometer, benchmark, and statement downloads) using exclusively official public sources.

---

## ⚠️ Disclaimer
> **Facts-only. No investment advice.** This assistant provides factual scheme details sourced from official public documents (AMC, SEBI, AMFI, and Kuvera support guides). It does not provide financial, tax, or investment advice, nor does it make performance claims or recommendations. Always refer to official Scheme Information Documents (SID) and Key Information Memorandums (KIM) before investing.

---

## 1. Scope & Corpus Definition
* **Selected AMC:** Mirae Asset Mutual Fund
* **Selected Schemes (4):**
  1. Mirae Asset Large Cap Fund (Large-cap)
  2. Mirae Asset Great Consumer Fund (Thematic / Consumption)
  3. Mirae Asset Tax Saver Fund (ELSS - Equity Linked Saving Scheme)
  4. Mirae Asset Focused Fund (Focused)
* **Corpus Size:** 18 verified public URLs spanning AMC SIDs, KIMs, monthly factsheets, AMFI riskometer guidelines, and Kuvera support documentation.

---

## 2. Source List (18 Official Public URLs)

| No. | Title / Document Type | Official URL |
| :--- | :--- | :--- |
| 1 | Mirae Asset Large Cap Fund - SID | `https://www.miraeassetmf.co.in/downloads/scheme-information-document` |
| 2 | Mirae Asset Great Consumer Fund - SID | `https://www.miraeassetmf.co.in/downloads/scheme-information-document` |
| 3 | Mirae Asset Tax Saver Fund - SID (ELSS) | `https://www.miraeassetmf.co.in/downloads/scheme-information-document` |
| 4 | Mirae Asset Focused Fund - SID | `https://www.miraeassetmf.co.in/downloads/scheme-information-document` |
| 5 | Mirae Asset Monthly Factsheet | `https://www.miraeassetmf.co.in/downloads/factsheet` |
| 6 | Mirae Asset KIM & Application Form | `https://www.miraeassetmf.co.in/downloads/key-information-memorandum` |
| 7 | Mirae Asset Fund Pricing & Expense Structure | `https://www.miraeassetmf.co.in/statutory-disclosure/total-expense-ratio` |
| 8 | SEBI Mutual Funds Regulations & Guidelines | `https://www.sebi.gov.in/sebiweb/home/HomeAction.do?sid=3` |
| 9 | AMFI Riskometer Guidelines & Definitions | `https://www.amfiindia.com/investor-corner/knowledge-center/riskometer.html` |
| 10 | Kuvera Help Center: How to download Capital Gains statement | `https://support.kuvera.in/support/solutions/` |
| 11 | Kuvera Help Center: Finding SIP details and minimums | `https://support.kuvera.in/support/solutions/` |
| 12 | Kuvera Help Center: Understanding Exit Loads | `https://support.kuvera.in/support/solutions/` |
| 13 | SEBI Master Circular for Mutual Funds | `https://www.sebi.gov.in/sebiweb/home/HomeAction.do?sid=3` |
| 14 | Mirae Asset Tax Saver Fund Lock-in details | `https://www.miraeassetmf.co.in/mutual-fund/equity/mirae-asset-tax-saver-fund` |
| 15 | Mirae Asset Large Cap Fund Benchmark & Riskometer | `https://www.miraeassetmf.co.in/mutual-fund/equity/mirae-asset-large-cap-fund` |
| 16 | AMFI Central Web-listing of NAVs & Benchmarks | `https://www.amfiindia.com/research-information/other-data/net-asset-value-nav` |
| 17 | Kuvera FAQ: Statement of Account (SOA) generation | `https://support.kuvera.in/support/solutions/` |
| 18 | Mirae Asset Service Requests & Forms Hub | `https://www.miraeassetmf.co.in/downloads/forms` |

---

## 3. Sample Q&A Dataset

### Query 1: Expense Ratio
* **User Question:** What is the expense ratio for Mirae Asset Large Cap Fund?
* **Assistant Answer:** The Total Expense Ratio (TER) varies by plan (Direct vs. Regular) and is updated periodically in accordance with SEBI limits based on daily net assets. You can view the exact daily updated slab-wise expense ratios directly on the official disclosure portal. Last updated from sources: October 2026.
* **Source Link:** [Mirae Asset TER Disclosures](https://www.miraeassetmf.co.in/statutory-disclosure/total-expense-ratio)

### Query 2: Exit Load
* **User Question:** What is the exit load for Mirae Asset Focused Fund?
* **Assistant Answer:** For Mirae Asset Focused Fund, an exit load may be levied if units are redeemed or switched out within a specified timeframe from the date of allotment, as detailed in the scheme document. Please refer to the latest Scheme Information Document (SID) or monthly factsheet for exact percentage slabs. Last updated from sources: October 2026.
* **Source Link:** [Mirae Asset Scheme Information Documents](https://www.miraeassetmf.co.in/downloads/scheme-information-document)

### Query 3: Minimum SIP
* **User Question:** What is the minimum SIP amount for Mirae Asset Tax Saver Fund?
* **Assistant Answer:** The minimum SIP investment amount for Mirae Asset Tax Saver Fund is typically ₹500 with daily, weekly, monthly, or quarterly frequency options. Kindly review the Fund KIM for any recent transaction limit revisions. Last updated from sources: October 2026.
* **Source Link:** [Mirae Asset KIM & Application Form](https://www.miraeassetmf.co.in/downloads/key-information-memorandum)

### Query 4: ELSS Lock-in
* **User Question:** What is the lock-in period for Mirae Asset Tax Saver Fund?
* **Assistant Answer:** Mirae Asset Tax Saver Fund is an Equity Linked Saving Scheme (ELSS) which carries a mandatory statutory lock-in period of 3 years from the date of unit allotment under Section 80C. No redemptions or switches are permitted during this lock-in window. Last updated from sources: October 2026.
* **Source Link:** [Mirae Asset Tax Saver Fund Overview](https://www.miraeassetmf.co.in/mutual-fund/equity/mirae-asset-tax-saver-fund)

### Query 5: Riskometer & Benchmark
* **User Question:** What is the riskometer rating and benchmark for Mirae Asset Great Consumer Fund?
* **Assistant Answer:** Mirae Asset Great Consumer Fund is assigned a "Very High" riskometer rating reflecting its thematic equity exposure, and is benchmarked against NIFTY India Consumption TRI. Scheme riskometers are evaluated and updated monthly in the official factsheet. Last updated from sources: October 2026.
* **Source Link:** [Mirae Asset Monthly Factsheet](https://www.miraeassetmf.co.in/downloads/factsheet)

### Query 6: Statement Download
* **User Question:** How can I download my capital gains statement through Kuvera?
* **Assistant Answer:** You can download your capital-gains statement on Kuvera by navigating to your Profile section, selecting Documents, and choosing Capital Gains to generate and download the report for your chosen financial year. No PII is stored or processed by this assistant. Last updated from sources: October 2026.
* **Source Link:** [Kuvera Support Center](https://support.kuvera.in/support/solutions/)

---

## 4. Setup Steps & Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/kuvera-mf-faq-assistant.git
   cd kuvera-mf-faq-assistant
   ```

2. **Install Dependencies:**
   ```bash
   pip install streamlit langchain chromadb sentence-transformers
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

---

## 5. Known Limits & Guardrails
* **No Advice Refusal:** Opinionated or portfolio-specific questions (e.g., *"Should I buy or sell this fund?"*) trigger a polite refusal: *"I provide factual scheme details only and cannot offer investment advice. Please consult a SEBI-registered advisor."*
* **PII Protection:** Inputs are strictly scanned and filtered; no PAN, Aadhaar, account numbers, OTPs, emails, or phone numbers are accepted or stored.
* **No Performance Claims:** Returns calculations are omitted; users are directed to official factsheets.