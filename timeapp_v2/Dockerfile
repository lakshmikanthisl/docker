# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install Flask pytz

# Expose port 80 to allow external connections
EXPOSE 80

# Run the Python app
CMD ["python", "app.py"]

