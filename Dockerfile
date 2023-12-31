FROM python:3.9.13

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/

CMD ["python", "app.py"]
