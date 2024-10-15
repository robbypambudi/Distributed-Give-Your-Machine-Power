# Use the official Python base image
FROM python:3.9-slim

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Jupyter and some common data science libraries
RUN pip install --no-cache-dir \
    jupyterlab \
    numpy \
    pandas \
    matplotlib \
    scikit-learn \
    seaborn

# Create a working directory
WORKDIR /workspace

# Expose the port Jupyter uses
EXPOSE 8888

# Run Jupyter Lab with options to allow access from outside the container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
