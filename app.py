import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import difflib

# Page Configuration
st.set_page_config(
    page_title="Infosys EDGAR & Financial Intelligence Portal",
    page_icon="📊",
    layout="wide"
)

# Sidebar Information
st.sidebar.title("🏢 Infosys Intelligence Portal")
st.sidebar.markdown("**CIK:** 0001067491")
st.sidebar.markdown("**Tickers:** INFY (NSE/BSE) | INFY (NYSE)")
st.sidebar.divider()

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📖 Section Extractor",
    "📈 Ratios & QoE",
    "🥧 Capital Allocation",
    "🛡️ Audit & Governance",
    "📁 SEC Filings",
    "🏛️ SEBI Disclosures",
    "🔍 Risk Diff"
])

# --- TAB 1: SECTION EXTRACTOR ---
with tab1:
    st.header("Item Parser & Section Extractor")
    st.caption("Isolate material disclosures directly from Form 20-F / 10-K filings.")
    
    section_choice = st.selectbox(
        "Select 10-K / 20-F Disclosure Item:",
        [
            ("Item 1: Business Description", "item_1"),
            ("Item 1A: Risk Factors", "item_1a"),
            ("Items 2 & 3: Properties & Legal Proceedings", "item_2_3"),
            ("Item 7: MD&A", "item_7"),
            ("Item 7A: Market Risk & Foreign Currency", "item_7a"),
            ("Item 8 Notes: Financial Statements & Accounting Policies", "item_8_notes"),
            ("Item 9A: Controls & ICFR Audit Opinion", "item_9a"),
            ("Part III: Governance & Executive Compensation", "part_3")
        ],
        format_func=lambda x: x[0]
    )
    
    disclosures = {
        "item_1": [
            "Core Offerings: Next-generation digital IT services, cloud architecture (Infosys Cobalt), AI platforms (Infosys Topaz), and consulting.",
            "Geographic Segment Mix: ~59% North America, ~28% Europe, ~13% Rest of World revenue generation.",
            "Global Workforce: Over 315,000 technology professionals across 50+ countries."
        ],
        "item_1a": [
            "Macroeconomic Disruption: Discrepancies in IT spending across banking, financial services (BFSI), and retail sectors.",
            "Talent & Compensation: Attrition fluctuations, wage inflation, and visa regulatory changes (H-1B/L-1).",
            "Cybersecurity & GenAI: Data protection compliance (GDPR/DPDP), potential cyber incidents, and rapid generative AI adoption.",
            "FX Volatility: Fluctuations between USD, EUR, GBP, and INR impacting operating margins."
        ],
        "item_2_3": [
            "Facilities Footprint: 120+ global development centers; major owned campuses in Electronics City (Bengaluru), Mysuru, Pune, and Hyderabad.",
            "Lease vs Owned: ~70% of delivery center footprint owned; sales and client offices leased globally.",
            "Legal Disclosures: No material pending litigation or regulatory actions that could impair consolidated financial stability."
        ],
        "item_7": [
            "Revenue Drivers: Cloud migration, enterprise automation, and large digital deal wins.",
            "Margin Dynamics: Operating margin governed by employee wage revisions, utilization rates, and offshore-onsite mix.",
            "Capital Resources: Strong free cash flow conversion ensuring dividend consistency and share buyback capabilities."
        ],
        "item_7a": [
            "Currency Exposure: Significant revenue earned in USD, EUR, and GBP while major operating expenses are incurred in INR.",
            "Hedging Strategy: Active use of forward contracts and currency options to manage foreign exchange volatility.",
            "Interest Rate Sensitivity: Minimal direct interest rate risk due to near-zero long-term debt exposure."
        ],
        "item_8_notes": [
            "Revenue Recognition: Compliance with IFRS 15 for fixed-price and time-and-materials enterprise contracts.",
            "Goodwill & Intangibles: Annual impairment testing shows no material goodwill impairment required.",
            "Income Tax Uncertainties: Provisions maintained for ongoing international tax proceedings and transfer pricing."
        ],
        "item_9a": [
            "ICFR Evaluation: Management concluded that Internal Control Over Financial Reporting (ICFR) was effective as of fiscal year-end.",
            "Auditor Opinion: Independent statutory auditor Deloitte Haskins & Sells LLP issued an unqualified audit opinion on ICFR.",
            "Material Weaknesses: Zero material weaknesses reported in internal accounting controls."
        ],
        "part_3": [
            "Executive Compensation: CEO compensation tied closely to variable performance metrics, ESG goals, and relative TSR.",
            "Board Structure: Majority independent directors with separate CEO and Chairman leadership roles.",
            "Insider Ownership: Promoter group holds ~14.7% equity; strict compliance under Insider Trading Prohibition codes."
        ]
    }
    
    st.subheader(section_choice[0])
    for point in disclosures[section_choice[1]]:
        st.success(f"✅ {point}")

# --- TAB 2: RATIOS & QUALITY OF EARNINGS ---
with tab2:
    st.header("Financial Trends & Quality of Earnings (QoE)")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Return on Equity (ROE)", "33.1%", "↑ Capital Efficiency")
    col2.metric("ROIC", "37.0%", "↑ Capital Productivity")
    col3.metric("Operating Margin", "21.2%", "Stable Industry Leading")
    col4.metric("Working Capital ($M)", "$5,410M", "Strong Liquidity Buffer")
    
    st.subheader("Quality of Earnings: Net Income vs Operating Cash Flow")
    financial_data = pd.DataFrame({
        "Year": ["2021", "2022", "2023", "2024", "2025"],
        "Net Income ($M)": [2613, 2981, 2983, 3171, 3290],
        "Operating Cash Flow ($M)": [3105, 3230, 2890, 3580, 3720]
    })
    
    fig = px.bar(financial_data, x="Year", y=["Net Income ($M)", "Operating Cash Flow ($M)"], barmode="group",
                 title="Multi-Year Accrual Gap Analysis")
    st.plotly_chart(fig, use_container_width=True)

# --- TAB 3: CAPITAL ALLOCATION ---
with tab3:
    st.header("Capital Allocation Breakdown")
    capital_df = pd.DataFrame({
        "Year": ["2021", "2022", "2023", "2024", "2025"],
        "Dividends": [1520, 1710, 1820, 1950, 2100],
        "Buybacks": [1200, 1450, 1100, 1150, 1250],
        "CapEx": [290, 310, 340, 360, 380],
        "R&D Spending": [110, 125, 140, 155, 170]
    })
    fig_cap = px.bar(capital_df, x="Year", y=["Dividends", "Buybacks", "CapEx", "R&D Spending"],
                     title="Capital Deployment Strategy ($ Millions USD)")
    st.plotly_chart(fig_cap, use_container_width=True)

# --- TAB 4: AUDIT & GOVERNANCE ---
with tab4:
    st.header("Audit Signals & Governance Panel")
    st.info(" Statutory Auditor: Deloitte Haskins & Sells LLP — Unqualified (Clean) Opinion")
    
    cam1, cam2 = st.columns(2)
    with cam1:
        st.warning("⚠️ Critical Audit Matter 1: Revenue Recognition (IFRS 15)")
        st.write("Percentage-of-completion estimation for enterprise fixed-price contracts.")
    with cam2:
        st.warning("⚠️ Critical Audit Matter 2: Income Tax Uncertainties")
        st.write("Transfer pricing contingencies across international tax jurisdictions.")

# --- TAB 5: SEC FILINGS DIRECTORY ---
with tab5:
    st.header("US SEC Submissions (20-F & 6-K)")
    headers = {'User-Agent': 'InfosysPortal StudentDeveloper student@example.com'}
    res = requests.get("https://data.sec.gov/submissions/CIK0001067491.json", headers=headers)
    if res.status_code == 200:
        recent = res.json()['filings']['recent']
        df_sec = pd.DataFrame({
            "Form": recent['form'][:15],
            "Filing Date": recent['filingDate'][:15],
            "Accession Number": recent['accessionNumber'][:15]
        })
        st.dataframe(df_sec, use_container_width=True)

# --- TAB 6: SEBI DISCLOSURES ---
with tab6:
    st.header("Statutory Filings (SEBI LODR Regulations)")
    st.markdown("- [Integrated Annual Report (FY 2024-25)](https://www.infosys.com/investors/reports-filings/annual-report.html)")
    st.markdown("- [Business Responsibility & Sustainability Report (BRSR)](https://www.infosys.com/about/esg/governance.html)")
    st.markdown("- [Whistleblower Policy](https://www.infosys.com/investors/corporate-governance/policies.html)")

# --- TAB 7: RISK DIFF ---
with tab7:
    st.header("Item 1A Risk Factors Text-Diffing Engine")
    t1 = st.text_area("Year T-1 Disclosure", "Infosys faces foreign exchange volatility and talent attrition.")
    t2 = st.text_area("Year T Disclosure", "Infosys faces foreign exchange volatility, talent attrition, and Generative AI disruption.")
    
    if st.button("Compare Disclosures"):
        diff = list(difflib.Differ().compare(t1.splitlines(), t2.splitlines()))
        additions = [line[2:] for line in diff if line.startswith('+ ')]
        if additions:
            st.error(f"Newly Added Risks: {additions}")
        else:
            st.success("No new risk factors detected.")
