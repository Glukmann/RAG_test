FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY admin_ui ./admin_ui

ENV PYTHONPATH=/app
ENV ADMIN_UI_HOST=0.0.0.0
ENV ADMIN_UI_PORT=8080

EXPOSE 8080

CMD ["python", "-m", "admin_ui.main"]
