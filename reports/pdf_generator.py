from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime
import os


def generate_pdf_report(contract_info, clauses, contract_risk, entities):
    """
    Generates a simple, readable PDF risk report.
    Returns the file path.
    """

    os.makedirs("reports/output", exist_ok=True)
    file_path = "reports/output/contract_risk_report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    # -------------------------
    # Title
    # -------------------------
    story.append(Paragraph(
        "<b>Contract Risk Assessment Report</b>",
        styles["Title"]
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        f"Generated on: {datetime.now().strftime('%d %B %Y, %H:%M')}",
        styles["Normal"]
    ))
    story.append(Spacer(1, 20))

    # -------------------------
    # Contract Overview
    # -------------------------
    story.append(Paragraph("<b>Contract Overview</b>", styles["Heading2"]))
    story.append(Spacer(1, 10))

    overview_data = [
        ["Contract Type", contract_info["type"]],
        ["Confidence", f"{int(contract_info['confidence'] * 100)}%"],
        ["Overall Risk Level", contract_risk["level"]],
        ["Risk Score", f"{contract_risk['score']:.2f} / 3.0"]
    ]

    overview_table = Table(overview_data, colWidths=[180, 280])
    overview_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("FONT", (0, 0), (-1, -1), "Helvetica")
    ]))

    story.append(overview_table)
    story.append(Spacer(1, 20))

    # -------------------------
    # Entities (optional but nice)
    # -------------------------
    story.append(Paragraph("<b>Key Extracted Information</b>", styles["Heading2"]))
    story.append(Spacer(1, 10))

    entity_text = f"""
    <b>Parties:</b> {', '.join(entities.get('parties', [])) or 'Not detected'}<br/>
    <b>Dates:</b> {', '.join(entities.get('dates', [])) or 'Not detected'}<br/>
    <b>Amounts:</b> {', '.join(entities.get('amounts', [])) or 'Not detected'}<br/>
    <b>Jurisdiction:</b> {', '.join(entities.get('jurisdiction', [])) or 'Not detected'}
    """

    story.append(Paragraph(entity_text, styles["Normal"]))
    story.append(Spacer(1, 20))

    # -------------------------
    # Clause Risk Table
    # -------------------------
    story.append(Paragraph("<b>Clause Risk Analysis</b>", styles["Heading2"]))
    story.append(Spacer(1, 10))

    table_data = [["Clause Type", "Risk Level", "Reason"]]

    for c in clauses:
        table_data.append([
            c["category"],
            c["risk"],
            c["reason"]
        ])

    clause_table = Table(table_data, colWidths=[120, 80, 260])
    clause_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONT", (0, 0), (-1, -1), "Helvetica"),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold")
    ]))

    story.append(clause_table)
    story.append(Spacer(1, 20))

    # -------------------------
    # Disclaimer
    # -------------------------
    story.append(Paragraph("<b>Disclaimer</b>", styles["Heading2"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "This report provides automated risk insights based on predefined rules "
        "and does not constitute legal advice. Users are encouraged to consult "
        "a qualified legal professional before making decisions.",
        styles["Normal"]
    ))

    # -------------------------
    # Build PDF
    # -------------------------
    doc.build(story)

    return file_path
