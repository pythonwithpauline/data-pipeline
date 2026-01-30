FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml /app/
COPY src/ /app/src/

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["download-service"]
