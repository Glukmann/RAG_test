#!/bin/bash
set -e

PROJECT_DIR="/Users/lipanovav/rag"
LOG_FILE="/tmp/rag-docker.log"

cd "$PROJECT_DIR"

# Wait for Docker daemon to become available
for i in $(seq 1 60); do
  if /usr/local/bin/docker info >/dev/null 2>&1; then
    echo "$(date): Docker is ready" >> "$LOG_FILE"
    break
  fi
  echo "$(date): Waiting for Docker daemon... ($i/60)" >> "$LOG_FILE"
  sleep 2
done

if ! /usr/local/bin/docker info >/dev/null 2>&1; then
  echo "$(date): Docker daemon not available, exiting" >> "$LOG_FILE"
  exit 1
fi

echo "$(date): Starting RAG services..." >> "$LOG_FILE"
/usr/local/bin/docker compose up -d >> "$LOG_FILE" 2>&1
echo "$(date): RAG services started" >> "$LOG_FILE"
