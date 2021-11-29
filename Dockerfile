FROM python:3.9

WORKDIR /home/fakebook

COPY requirements.txt requirements.txt
RUN python -m venv virtualenv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY run.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]