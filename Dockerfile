FROM python:3.14-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./

RUN pip install --no-cache-dir pytest pytest-bdd

COPY src/ ./src/
COPY tests/ ./tests/

CMD ["pytest", "-q"]
