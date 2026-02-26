#!/usr/bin/env python3
"""Convert product brief markdown to PDF using reportlab."""
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def escape(s: str) -> str:
    """Escape & < > for ReportLab Paragraph XML."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bold_to_xml(s: str) -> str:
    """Convert **text** to <b>text</b> (call after escape)."""
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)


def to_para_text(s: str) -> str:
    return bold_to_xml(escape(s))


def parse_md(md_path: Path) -> list:
    """Parse markdown into a list of (block_type, content)."""
    text = md_path.read_text(encoding="utf-8")

    # Strip YAML frontmatter
    if text.startswith("---"):
        end = text.index("---", 3) + 3
        text = text[end:].lstrip()

    # Strip HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    blocks = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        if stripped.startswith("# "):
            blocks.append(("h1", stripped[2:].strip()))
            i += 1
            continue
        if stripped.startswith("## "):
            blocks.append(("h2", stripped[3:].strip()))
            i += 1
            continue
        if stripped.startswith("### "):
            blocks.append(("h3", stripped[4:].strip()))
            i += 1
            continue
        if stripped.startswith("#### "):
            blocks.append(("h4", stripped[5:].strip()))
            i += 1
            continue
        if stripped == "---":
            blocks.append(("hr", None))
            i += 1
            continue
        if stripped.startswith("| ") and "|" in stripped[1:]:
            # Table: collect all consecutive table rows
            table_rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = [cell.strip() for cell in lines[i].strip().split("|")[1:-1]]
                # Skip separator line (|---|---|)
                if row and not re.match(r"^[-:\s]+$", "".join(row)):
                    table_rows.append(row)
                i += 1
            if table_rows:
                blocks.append(("table", table_rows))
            continue
        if stripped.startswith("- "):
            # Bullet list: collect consecutive bullets
            bullets = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                bullets.append(lines[i].strip()[2:].strip())
                i += 1
            blocks.append(("ul", bullets))
            continue

        # Paragraph: collect until blank or next block
        para_lines = []
        while i < len(lines):
            ln = lines[i]
            if not ln.strip():
                i += 1
                break
            if (
                ln.strip().startswith("#")
                or ln.strip().startswith("- ")
                or ln.strip().startswith("| ")
                or ln.strip() == "---"
            ):
                break
            para_lines.append(ln.strip())
            i += 1
        if para_lines:
            blocks.append(("p", " ".join(para_lines)))

    return blocks


def build_pdf(blocks: list, out_path: Path, styles) -> None:
    """Build PDF from parsed blocks."""
    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )
    story = []

    for kind, content in blocks:
        if kind == "h1":
            story.append(Paragraph(to_para_text(content), styles["Title"]))
            story.append(Spacer(1, 0.2 * inch))
        elif kind == "h2":
            story.append(Spacer(1, 0.15 * inch))
            story.append(Paragraph(to_para_text(content), styles["Heading1"]))
            story.append(Spacer(1, 0.1 * inch))
        elif kind == "h3":
            story.append(Paragraph(to_para_text(content), styles["Heading2"]))
            story.append(Spacer(1, 0.08 * inch))
        elif kind == "h4":
            story.append(Paragraph(to_para_text(content), styles["Heading3"]))
            story.append(Spacer(1, 0.06 * inch))
        elif kind == "hr":
            story.append(Spacer(1, 0.15 * inch))
        elif kind == "p":
            story.append(Paragraph(to_para_text(content), styles["Normal"]))
            story.append(Spacer(1, 0.08 * inch))
        elif kind == "ul":
            for item in content:
                story.append(
                    Paragraph("• " + to_para_text(item), styles["Normal"])
                )
                story.append(Spacer(1, 0.04 * inch))
        elif kind == "table":
            # Table cells as Paragraphs for bold
            table_data = []
            for row in content:
                table_data.append([Paragraph(to_para_text(c), styles["Normal"]) for c in row])
            t = Table(table_data, colWidths=[1.2 * inch, 4.3 * inch])
            t.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTSIZE", (0, 0), (-1, 0), 10),
                        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                        ("TOPPADDING", (0, 0), (-1, 0), 8),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("FONTSIZE", (0, 0), (-1, -1), 9),
                        ("LEFTPADDING", (0, 0), (-1, -1), 6),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ]
                )
            )
            story.append(t)
            story.append(Spacer(1, 0.15 * inch))

    doc.build(story)


def main() -> None:
    base = Path(__file__).resolve().parent.parent
    md_path = base / "_bmad-output/planning-artifacts/product-brief-air-pods-cohort-1-2026-02-19.md"
    out_dir = base / "docs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "product-brief-air-pods-cohort-1-2026-02-19.pdf"

    if len(sys.argv) > 1:
        md_path = Path(sys.argv[1])
    if len(sys.argv) > 2:
        out_path = Path(sys.argv[2])

    styles = getSampleStyleSheet()
    blocks = parse_md(md_path)
    build_pdf(blocks, out_path, styles)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
