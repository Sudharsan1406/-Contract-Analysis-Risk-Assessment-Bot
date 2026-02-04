# 🧠 GenAI-Powered Contract Risk Assessment Bot

A **GenAI-driven legal assistant** designed to help **Indian Small and Medium Businesses (SMEs)** understand complex contracts, identify legal risks, and receive **actionable advice in plain language**. The system analyzes contracts clause-by-clause, assigns risk scores, suggests safer alternatives, and generates professional reports for legal consultation.

---

## 🚀 Features

- 📄 **Multi-format Contract Upload**: PDF, DOCX, TXT
- 🌐 **Multilingual Support**: English & Hindi (auto-detection + normalization)
- 🧩 **Clause-by-Clause Analysis**
- ⚠️ **Risk Scoring Engine** (Low / Medium / High)
- 🧠 **Plain-English Explanations** for legal clauses
- ✍️ **Alternative Clause Suggestions** for risky terms
- 🇮🇳 **Indian Law Awareness** (employment, termination, indemnity, penalties, etc.)
- 📊 **Overall Contract Risk Score**
- 🧾 **Named Entity Extraction** (parties, dates, obligations)
- 📥 **Downloadable PDF Risk Report**
- 🔐 **Confidential by Design** (no data persistence)
- 🧪 **Audit-ready structured outputs**

---

## 🏢 Supported Contract Types

- Employment Agreements
- Vendor / Supplier Contracts
- Lease Agreements
- Partnership Deeds
- Service Agreements

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – UI
- **spaCy / NLP** – Clause processing & NER
- **Rule-based + Heuristic Risk Engine**
- **ReportLab** – PDF generation

---

## 📂 Project Structure

```
hackathon2/
│
├── app.py                     # Streamlit application
│
├── core/
│   ├── __init__.py
│   ├── text_extractor.py      # PDF/DOCX/TXT extraction
│   ├── language.py            # Language detection & normalization
│   ├── contract_classifier.py
│   ├── clause_splitter.py     # Clause segmentation
│   ├── ner_extractor.py       # Entity extraction
│   ├── risk_engine.py         # Risk scoring logic
│   ├── explainer.py           # Plain-English explanations
│
├── reports/
│   ├── pdf_generator.py       # PDF report creation
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

Required libraries:
- streamlit
- reportlab
- langdetect
- spacy
- python-docx
- PyPDF2

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open the browser URL shown in terminal.

---

## 📄 Usage Guidelines

- Upload **text-based PDFs** (not scanned images)
- DOCX or TXT files are recommended for best accuracy
- Minimum content: **50+ characters**

Example `.txt` input:
```
The company may terminate the agreement without notice.
The employee shall indemnify the company for all losses.
Early termination attracts a penalty.
```

---

## 📊 Output

- Contract overview (type, confidence, language)
- Overall risk score
- Clause-wise risk table
- Plain-English explanations
- Suggested safer alternatives
- Downloadable **PDF risk report**

---

## 🔐 Confidentiality & Ethics

- No contract data is stored
- Processing happens in-memory only
- Suitable for legal review preparation (not legal advice)

---

## ⚠️ Disclaimer

This tool **does not replace a lawyer**. It is intended to assist SMEs in understanding contracts and preparing for professional legal consultation.

---

## 👤 Author

**Sudharsan M S**

---

## 🏁 Hackathon Readiness

✔ Live UI
✔ Risk Engine
✔ Explainability
✔ PDF Export
✔ Indian SME-focused use case

---

Feel free to extend with:
- LLM-based clause reasoning
- Legal knowledge base
- Compliance checklist per law
- Contract template generator

