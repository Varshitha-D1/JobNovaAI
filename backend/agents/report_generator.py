from fpdf import FPDF


def clean_text(text):

    replacements = {
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        "•": "-",
        "✓": "[OK]",
        "❌": "[X]",
        "⚖️": "[JUDGE]",
        "✅": "[OK]",
        "📄": "",
        "📊": "",
        "🎤": "",
        "🧠": ""
    }

    text = str(text)

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.encode(
        "latin-1",
        "replace"
    ).decode(
        "latin-1"
    )


def generate_report(
    candidate_name,
    summary,
    skill_analysis,
    questions,
    hire_result,
    reject_result,
    final_decision
):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)

    pdf.cell(
        200,
        10,
        txt=f"CandidateIQ Report - {candidate_name}",
        ln=True
    )

    sections = [
        ("Candidate Summary", summary),
        ("Skill Gap Analysis", skill_analysis),
        ("Interview Questions", questions),
        ("Hire Agent", hire_result),
        ("Reject Agent", reject_result),
        ("Judge Verdict", final_decision)
    ]

    for title, content in sections:

        pdf.ln(5)

        pdf.set_font(
            "Arial",
            "B",
            12
        )

        pdf.cell(
            200,
            10,
            txt=clean_text(title),
            ln=True
        )

        pdf.set_font(
            "Arial",
            size=11
        )

        pdf.multi_cell(
            0,
            8,
            txt=clean_text(content)
        )

    filename = (
        f"{candidate_name}_report.pdf"
    )

    pdf.output(filename)

    return filename