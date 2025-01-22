# Start with a lightweight Python base image
FROM python:3.9-slim

# Install Rust if you want to build the contract inside the container
RUN apt-get update && apt-get install -y --no-install-recommends \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory
WORKDIR /usr/src/app

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose Flask's default port
EXPOSE 8080

# Default command (used if you run `docker run ...` without docker-compose)
CMD ["bash", "-c", "cd ai_nft && python main.py"]
