import pdfplumber
from docx import Document


def extract_text(uploaded_file):
    """
    Extract text from PDF, DOCX, or TXT files.
    Returns extracted text or empty string.
    """

    file_name = uploaded_file.name.lower()

    try:
        # ---- PDF ----
        if file_name.endswith(".pdf"):
            text = ""
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text.strip()

        # ---- DOCX ----
        elif file_name.endswith(".docx"):
            doc = Document(uploaded_file)
            return "\n".join([para.text for para in doc.paragraphs]).strip()

        # ---- TXT ----
        elif file_name.endswith(".txt"):
            return uploaded_file.read().decode("utf-8").strip()

        else:
            return ""

    except Exception as e:
        return ""
