# Use an official Python runtime as a parent image
#FROM python:3.11
FROM python:3.11.7-slim-bookworm
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r r.txt

# Make port 8089 available to the world outside this container
EXPOSE 5000

# Define environment variable

ENV FLASK_APP main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
