FROM python:3.6

ENV BROKER_URL=redis://redis:6379/0
ENV RESULT_BACKEND=redis://redis:6379/0

COPY requirements.txt /queue/
WORKDIR /queue

RUN pip install -r requirements.txt

ENTRYPOINT celery -A tasks worker --loglevel=info