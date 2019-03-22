FROM python:3.6

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src

COPY ./src .
VOLUME [ "/app/src" ]

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD [ "flask", "run", "--reload", "--host", "0.0.0.0", "--port", "5000", "--eager-loading", "--debugger" ]
#CMD ["python","app.py"]
