# Use an official Python runtime as a base image
FROM pypy:latest

# Set environment variables (optional but recommended)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (if needed)
# For example, if you use PostgreSQL, you may need to install its client library
# RUN apt-get update && apt-get install -y libpq-dev

# Copy the requirements file and install Python dependencies

COPY requirements.txt requirements.txt 
RUN /bin/sh -c pip3 install -r./requirements.txt
# Copy the Django project code into the container
COPY . /app/

# Run Django's collectstatic (if needed)
# RUN python manage.py collectstatic --noinput

# Expose the port that Django runs on (optional)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
