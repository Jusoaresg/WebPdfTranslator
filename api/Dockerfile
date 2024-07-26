FROM python

WORKDIR /usr/src/app

COPY src/ ./

RUN apt-get update && \
    apt-get install -y libreoffice-writer-nogui && \
    apt-get clean 

RUN pip install --no-cache-dir -r requirements.txt

CMD fastapi run app.py
