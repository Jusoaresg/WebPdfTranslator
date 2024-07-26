from fastapi import FastAPI, Response, UploadFile
import aiofiles
from pdf_to_docx import converter
import uuid
import os

app = FastAPI()

@app.post("/translate")
async def translate(file: UploadFile):

    if not os.path.exists("./files"):
        os.makedirs("./files")

    pdfName = str(uuid.uuid4())
    filePath = f"./files/{pdfName}"

    async with aiofiles.open(filePath, "wb") as f:
        await f.write(file.file.read())

    await converter.init(filePath, pdfName)

    with open(f'./files/{pdfName}-outputTranslated.pdf', mode="rb") as pdfFile:
        pdfContent = pdfFile.read()

    try:
        os.remove(f'./files/{pdfName}')
        os.remove(f'./files/{pdfName}-outputTranslated.docx')
        os.remove(f'./files/{pdfName}-outputTranslated.pdf')
    except:
        raise Exception("ERROR WHEN DELETING FILES")

    return Response(content=pdfContent, media_type="application/pdf")
