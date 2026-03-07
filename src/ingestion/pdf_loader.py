import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


if __name__ == "__main__":
    sample_pdf = "data/raw/sample.pdf"
    text = extract_text_from_pdf(sample_pdf)

    print(text[:1000])

