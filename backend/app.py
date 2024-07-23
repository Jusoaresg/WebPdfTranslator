from fastapi import FastAPI, Response, UploadFile
from starlette.responses import FileResponse
import aiofiles
from converterDocxPdf import converter

app = FastAPI()

@app.post("/translate")
async def translate(file: UploadFile, sourceLang: str, destLang: str):
    filePath = f"./files/{'sample.pdf'}"
    async with aiofiles.open(filePath, "wb") as f:
        await f.write(file.file.read())

    await converter.init()
    #return FileResponse(path="./files/outputTranslated.pdf", media_type="application/octet-stream", filename="arquivo.pdf")
    with open("./files/outputTranslated.pdf", mode="rb") as pdfFile:
        pdfContent = pdfFile.read()
    return Response(content=pdfContent, media_type="application/pdf")
