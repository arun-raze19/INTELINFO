# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements (for best practice, but we only need Flask)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
