from translator  import translate_docx
from pdf2docx import Converter
import threading
from constants import colors
from pdf_to_docx import error_checker, page_counter


threadsToUse = 1
checkForErrors = ""

#pdfFile = "./files/sample.pdf"

errors = []

async def init(pdfFile):
    if(checkForErrors == ""):

        threads = []
        pages = page_counter.page_count(pdfFile)
        pagesDivided = pages/threadsToUse

        for i in range(threadsToUse):
            if (i == 0): 
                start = 0;
                end = pagesDivided

            else:
                start = i * pagesDivided
                end = (i + 1) * pagesDivided

            thread = threading.Thread(target=error_checker.error_check, args=(start, end))
            thread.start()
            threads.append(thread)

        for key, thread in enumerate(threads):
            thread.join()


        print(errors)


    if len(errors) == 0:
        cv = Converter(pdfFile)
        cv.convert("output.docx", start=0, end=page_counter.page_count(pdfFile), multi_processing=True, cpu_count=threadsToUse)
        cv.close()

    translate_docx.translate_docx(threadsToUse)
