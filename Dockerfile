FROM python:3.10

LABEL maintainer="kirill.sokolski3007@gmail.com"

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "task_1.py"]