import requests
from flask import Flask, Response, render_template, request
from dotenv import load_dotenv
import os

app = Flask("pdfTranslator")

load_dotenv()
api_url = str(os.getenv("TRANSLATOR_API_URL"))
#api_url = "http://127.0.0.1:8000/translate"

FILES_FOLDER = "./files/"
app.config['FILES_FOLDER'] = FILES_FOLDER

@app.route("/", methods=['GET', 'POST'])
def homePage():

    if request.method == 'POST':
        file = request.files["file"]

        body = { "file": (file.filename, file.stream, file.mimetype)}

        res = requests.post(url=api_url, files=body)

        res = Response(res.content, content_type="application/pdf")
        return res


    return render_template("index.html")
