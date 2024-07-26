import fitz

def page_count(pdfFile):
    pdf = fitz.open(pdfFile)
    pages = len(pdf)
    pdf.close()
    return pages
