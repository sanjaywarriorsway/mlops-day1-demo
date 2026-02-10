# 1. Base Image (Official Python Image)
FROM python:3.9-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy files from your laptop to the container
COPY requirements.txt .
COPY app.py .
COPY model.pkl .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port
EXPOSE 8000

# 6. Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]