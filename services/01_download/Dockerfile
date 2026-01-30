FROM python:3.11-slim

WORKDIR /app

COPY services/01_download /app/services/01_download
COPY configs /app/configs

RUN pip install --no-cache-dir -e /app/services/01_download

CMD ["download-service", "run", "--client", "acme"]
