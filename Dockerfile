# Use official Python image
FROM python:3.11-slim
# Set working directory inside the container
WORKDIR /app
# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the project files
COPY . .
# Expose port 8080 for the app
EXPOSE 8080
# Run the Django app using Gunicorn
CMD ["gunicorn", "payroll_system.wsgi:application", "--bind", "0.0.0.0:8080"]
