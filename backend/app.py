from fastapi import FastAPI, Response, UploadFile
from starlette.responses import FileResponse
import aiofiles
from converterDocxPdf import converter
import uuid
import os
import shutil

app = FastAPI()

@app.post("/translate")
async def translate(file: UploadFile):

    if not os.path.exists("./files"):
        os.makedirs("./files")

    filePath = f"./files/{uuid.uuid4()}"

    async with aiofiles.open(filePath, "wb") as f:
        await f.write(file.file.read())

    await converter.init(filePath)

    with open("./files/outputTranslated.pdf", mode="rb") as pdfFile:
        pdfContent = pdfFile.read()

    if os.path.exists("./files"):
        shutil.rmtree("./files")


    return Response(content=pdfContent, media_type="application/pdf")
