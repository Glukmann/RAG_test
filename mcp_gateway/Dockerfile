FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp_gateway ./mcp_gateway

ENV PYTHONPATH=/app
ENV MCP_LOG_LEVEL=INFO

CMD ["python", "-m", "mcp_gateway.server"]
