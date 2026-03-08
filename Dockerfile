FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/superbuilderbob/mock-incident-operation.git .

# Add UV package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

RUN uv sync --locked

CMD ["uv", "run", "streamlit", "run", "src/main.py"]