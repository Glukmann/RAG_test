FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp_server ./mcp_server

ENV PYTHONPATH=/app
ENV MCP_LOG_LEVEL=INFO

EXPOSE 3000

CMD ["python", "-m", "mcp_server.server"]
