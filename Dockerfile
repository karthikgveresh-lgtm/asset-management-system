# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy file into container
COPY hello.py .

# Run program
CMD ["python", "hello.py"]