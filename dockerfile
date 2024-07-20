FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    && pip install opencv-python-headless numpy

# Copy application files
COPY . /app
WORKDIR /app

# Run the application
CMD ["python", "app.py"]
