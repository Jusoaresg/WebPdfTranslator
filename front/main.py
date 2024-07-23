import webbrowser
import requests
from flask import Flask, Response, render_template, render_template_string, request, url_for, redirect

app = Flask("pdfTranslator")

api_url = "http://127.0.0.1:8000/translate"
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
