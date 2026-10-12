FROM python:3.12.3

WORKDIR /app

COPY . .

RUN pip install -r requirements-dev.txt

CMD ["python", "main.py"]