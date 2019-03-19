FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src

COPY ./src .
VOLUME [ "/app/src" ]

#CMD [ "flask", "run", "--no-reload" ]
CMD ["python3","app.py"]
