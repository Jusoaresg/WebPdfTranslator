FROM python

WORKDIR /usr/src/app

COPY ./* ./

RUN pip install --no-cache-dir -r requirements.txt

CMD flask --app main.py run
