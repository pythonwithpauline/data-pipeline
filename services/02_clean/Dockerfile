FROM python:3.11-slim

WORKDIR /app

COPY services/02_clean /app/services/02_clean
COPY configs /app/configs

RUN pip install --no-cache-dir -e /app/services/02_clean

CMD ["clean-service", "run", "--client", "acme"]
