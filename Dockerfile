FROM python:3.7-alpine

#RUN adduser -D par
#WORKDIR /home/parlay-rest
RUN apk --update add bash nano git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py ./
#RUN chown -R par:parlay-rest ./
#USER par
CMD uvicorn main:app --host 0.0.0.0 --port 5057
