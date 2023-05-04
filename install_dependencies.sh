#!/bin/bash

if ! command -v docker &> /dev/null; then
    echo "Docker not found, installing Docker..."
    brew install --cask docker
else
    echo "Docker already installed, skipping installation..."
fi

echo "Starting Docker Desktop..."
open /Applications/Docker.app

echo "Waiting for Docker to start..."
while ! docker system info > /dev/null 2>&1; do sleep 1; done

echo "Creating requirements.txt..."
cat > requirements.txt << EOL
Flask==2.1.1
sympy==1.9
cachetools==4.2.4
EOL

echo "Building Docker image..."
docker build -t math-api .

echo "Running Docker container..."
docker run -d --name math-api-container -p 8000:8000 math-api

echo "Done. The REST API is now accessible at http://localhost:8000"
