# Base Image: Use official lightweight Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & enable real-time output logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# et working directory inside the container
WORKDIR /app

# Install system dependencies required for PostgreSQL drivers
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies list first (leveraging Docker layer caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code into container
COPY config/ ./config/
COPY src/ ./src/
COPY sql/ ./sql/
COPY main.py .

# Entry point: command to run the ETL pipeline
CMD ["python", "main.py"]