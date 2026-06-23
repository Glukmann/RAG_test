FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY indexer ./indexer

ENV PYTHONPATH=/app
ENV INDEXER_API_HOST=0.0.0.0
ENV INDEXER_API_PORT=8001

EXPOSE 8001

CMD ["python", "-m", "indexer.main", "api"]
