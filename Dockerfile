# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy file into container
COPY hello.py .

# Run program
CMD ["python", "hello.py"]
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]