FROM python:3.6-alpine
RUN apk build-base
RUN adduser -D imdb

WORKDIR /home/imdb

COPY requirements.txt requirements.txt
RUN python -m venv imdb
RUN imdb/bin/pip install -r requirements.txt
RUN imdb/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY imdb.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP imdb.py

RUN chown -R imdb:imdb ./
USER imdb

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
