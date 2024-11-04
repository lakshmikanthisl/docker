# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python app code into the container
COPY app.py /app/app.py

# Install Flask
RUN pip install Flask

# Expose port 80 to allow external connections
EXPOSE 80

# Run the Python app
CMD ["python", "app.py"]

