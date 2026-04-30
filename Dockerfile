# Use official Python image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies for Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    tcl \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxft2 \
    libxss1 \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Default command to run your app
CMD ["python", "AceestApp.py"]