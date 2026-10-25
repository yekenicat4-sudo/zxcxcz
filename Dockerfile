FROM python:3.12-slim

WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-api.txt

# Expose port
EXPOSE 8000

# Run the API
CMD ["python", "api.py"]
