FROM python:3.11-slim

WORKDIR /app

# Install build dependencies for faiss and pickle
RUN apt-get update && apt-get install -y \
    build-essential \
    swig \
    gcc \
    libopenblas-dev \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080
EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
