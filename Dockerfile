# Use official Python slim image
FROM python:3.11-slim
# Set working directory
WORKDIR /app
# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy project files
COPY . .
# Expose port for Cloud Run
ENV PORT=8080
# Start Gunicorn with Django WSGI
CMD ["gunicorn", "-b", ":8080", "payroll_system.wsgi:application"]
