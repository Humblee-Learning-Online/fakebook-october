FROM python:3.9-buster

WORKDIR /home/fakebook

COPY requirements.txt requirements.txt
RUN python -m venv virtualenv
RUN virtualenv/bin/pip install --upgrade pip
RUN virtualenv/bin/pip install -r requirements.txt
RUN virtualenv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY run.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]