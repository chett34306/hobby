from tika import parser
import fitz


def pdftotextusingtika():
    raw_from_pdf = parser.from_file("test.pdf")
    raw_text = str(raw_from_pdf)
    safe_text = raw_text.encode(encoding='utf-8', errors='ignore')
    safe_text = str(safe_text).replace("\n","").replace("\\","")
    print(safe_text)

def pdftotextusingPyMuPDF():
    ifile = "test.pdf"
    doc = fitz.open(ifile)
    page_count = doc.pageCount
    page = 0
    text = ''
    while (page < page_count):
        p = doc.loadPage(page)
        page += 1
        text = text + p.getText()
    print(text)


if __name__ == "__main__":
    # pdftotextusingtika()
    pdftotextusingPyMuPDF()

