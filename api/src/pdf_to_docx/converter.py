from translator  import translate_docx
from pdf2docx import Converter
import threading
import pdf_to_docx


threadsToUse = 1
checkForErrors = []

errors = []

async def init(pdfPath: str, pdfName: str):

    threads = []
    pages = pdf_to_docx.page_count(pdfPath)
    pagesDivided = pages/threadsToUse

    for i in range(threadsToUse):
        if (i == 0): 
            start = 0;
            end = pagesDivided

        else:
            start = i * pagesDivided
            end = (i + 1) * pagesDivided

        thread = threading.Thread(target=pdf_to_docx.error_checker.error_check, args=(start, end))
        thread.start()
        threads.append(thread)

    for _, thread in enumerate(threads):
        thread.join()


    print(errors)


    if len(errors) == 0:
        cv = Converter(pdfPath)
        cv.convert(f'{pdfName}-output.docx', start=0, end=pdf_to_docx.page_counter.page_count(pdfPath), multi_processing=True, cpu_count=threadsToUse)
        cv.close()

    pdf_to_docx.translate_docx(threadsToUse, pdfName)
