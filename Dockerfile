FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Add --timeout 1000 to prevent read timeouts
RUN pip install --no-cache-dir --timeout 1000 -r requirements.txt

COPY . .

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]