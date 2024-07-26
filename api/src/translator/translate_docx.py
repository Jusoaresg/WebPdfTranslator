import subprocess
import threading
import docx
from translator import integer_checker, translate_paragraph
import os


def translate_docx(threadsToUse):
    doc = docx.Document("output.docx")

    print(len(doc.paragraphs))
    threads = []

    paragraphs = len(doc.paragraphs)
    dividedParagraphs = paragraphs//threadsToUse

    paragraphsExcluded = 0
    for _, p in enumerate(doc.paragraphs):
        if p.text != "" and not integer_checker.check_integer(p.text):
            paragraphsExcluded = paragraphsExcluded + 1

    for i in range(threadsToUse):
        if i == 0:
            start = 0
            end = dividedParagraphs
        else:
            start = dividedParagraphs*i
            end = start + dividedParagraphs + 1

        if i == threadsToUse-1:
            end = paragraphs

        thread = threading.Thread(target=translate_paragraph.translate_paragraph, args=(doc, start, end, ))
        threads.append(thread)
        thread.start()

    for _, thread in enumerate(threads):
        thread.join()


    doc.save("./files/outputTranslated.docx")


    subprocess.call(['soffice',
                    '--convert-to',
                    'pdf',
                    '--outdir',
                    './files',
                    './files/outputTranslated.docx'])

    try:
        os.remove("./output.docx")
    except:
        return
