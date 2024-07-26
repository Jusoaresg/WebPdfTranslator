from deep_translator import GoogleTranslator
from translator import integer_checker 


def translate_paragraph(doc, start, end):
    for i in range(start, end):
        paragraph = doc.paragraphs[i].text
        if(paragraph != "" and integer_checker.check_integer(paragraph) == False):
            translated = GoogleTranslator(source='en', target='pt').translate(doc.paragraphs[i].text)
            doc.paragraphs[i].text = translated
