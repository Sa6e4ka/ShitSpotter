FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "echo Starting container... && ls -l && uvicorn main:app --host 0.0.0.0 --port 8080"]

