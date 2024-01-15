FROM python:3.9

WORKDIR .

COPY . .

RUN pip3 install --upgrade pip -r requirements.txt

EXPOSE 80

CMD python app.py

