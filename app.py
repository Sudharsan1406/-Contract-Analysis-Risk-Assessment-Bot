import streamlit as st
from core.text_extractor import extract_text
from core.language import detect_language, normalize_to_english
from core.contract_classifier import classify_contract
from core.clause_splitter import split_into_clauses
from core.ner_extractor import extract_entities
from core.risk_engine import evaluate_clause_risk, compute_contract_risk
from core.explainer import explain_clause, suggest_alternative
from reports.pdf_generator import generate_pdf_report

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Contract Risk Assessment Bot",
    layout="wide"
)

# ---------------------------
# Title
# ---------------------------
st.title("📄 Contract Analysis & Risk Assessment Bot")
st.write(
    "Upload a contract to identify risky clauses and understand them in plain English."
)

# ---------------------------
# File upload
# ---------------------------
uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

# ---------------------------
# Analyze button
# ---------------------------
if uploaded_file and st.button("Analyze Contract"):

    with st.spinner("Analyzing contract..."):
        # ---------------------------
        # Step 1: Extract text
        # ---------------------------
        raw_text = extract_text(uploaded_file)

        if raw_text is None or len(raw_text.strip()) < 50:
            st.error(
                "Unable to extract text.\n\n"
                "Please upload a text-based PDF, DOCX, or TXT file."
            )
            st.stop()
        
        language = detect_language(raw_text)
        
        text = normalize_to_english(raw_text)
        
        if text is None or len(text.strip()) < 50:
            st.error("Text normalization failed.")
            st.stop()



        # ---------------------------
        # Step 2: Language detection
        # ---------------------------
        language = detect_language(raw_text)
        text = normalize_to_english(raw_text)

        # ---------------------------
        # Step 3: Contract classification
        # ---------------------------
        contract_info = classify_contract(text)

        # ---------------------------
        # Step 4: Clause segmentation
        # ---------------------------
        clauses = split_into_clauses(text)

        # ---------------------------
        # Step 5: Entity extraction
        # ---------------------------
        entities = extract_entities(text)

        # ---------------------------
        # Step 6: Risk analysis
        # ---------------------------
        analyzed_clauses = []
        for clause in clauses:
            risk = evaluate_clause_risk(clause)
            explanation = explain_clause(clause, risk)
            suggestion = suggest_alternative(clause, risk)
        
            analyzed_clauses.append({
                "clause_id": clause["clause_id"],
                "category": clause["category"],
                "text": clause["text"],
                "risk": risk["risk_level"],
                "reason": risk["reason"],
                "explanation": explanation,
                "suggestion": suggestion
            })


        contract_risk = compute_contract_risk(analyzed_clauses)

    # ---------------------------
    # RESULTS
    # ---------------------------
    st.success("Analysis completed")

    # ---------------------------
    # Contract overview
    # ---------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 Contract Overview")
        st.write(f"**Detected Type:** {contract_info['type']}")
        st.write(f"**Confidence:** {int(contract_info['confidence'] * 100)}%")
        st.write(f"**Language:** {'Hindi (translated)' if language == 'hi' else 'English'}")

    with col2:
        st.subheader("⚠️ Overall Risk")
        st.metric(
            label="Contract Risk Level",
            value=contract_risk["level"]
        )
        st.write(f"Risk Score: {contract_risk['score']:.2f} / 3.0")

    st.divider()

    # ---------------------------
    # Plain-English summary
    # ---------------------------
    st.subheader("📝 Plain-English Summary")

    high_risk_count = len([c for c in analyzed_clauses if c["risk"] == "High"])
    medium_risk_count = len([c for c in analyzed_clauses if c["risk"] == "Medium"])

    st.markdown(f"""
    - This is a **{contract_info['type']}**.
    - **{high_risk_count} high-risk** and **{medium_risk_count} medium-risk** clauses were found.
    - Some clauses may create an imbalance between the parties.
    - Review high-risk clauses carefully before signing.
    """)

    st.divider()

    # ---------------------------
    # Clause-by-clause table
    # ---------------------------
    st.subheader("📊 Clause Risk Breakdown")

    table_data = []
    for c in analyzed_clauses:
        table_data.append({
            "Clause Type": c["category"],
            "Risk": "🔴 High" if c["risk"] == "High"
                    else "🟠 Medium" if c["risk"] == "Medium"
                    else "🟢 Low",
            "Why it’s risky": c["reason"]
        })

    st.table(table_data)

    st.divider()

    # ---------------------------
    # Detailed explanations
    # ---------------------------
    st.subheader("🔍 Detailed Clause Analysis")

    for c in analyzed_clauses:
        with st.expander(f"{c['category']} | Risk: {c['risk']}"):
            st.markdown("**Original Clause**")
            st.write(c["text"])

            st.markdown("**Explanation (Plain English)**")
            st.write(c["explanation"])

            if c["risk"] != "Low":
                st.markdown("**Suggested Alternative**")
                st.write(c["suggestion"])

    st.divider()

    # ---------------------------
    # Download PDF
    # ---------------------------
    st.subheader("📥 Download Report")

    if st.button("Download PDF Risk Report"):
        pdf_path = generate_pdf_report(
            contract_info,
            analyzed_clauses,
            contract_risk,
            entities
        )
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name="contract_risk_report.pdf",
                mime="application/pdf"
            )
