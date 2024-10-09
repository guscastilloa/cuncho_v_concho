# Use base image with Python
FROM python:3.9.16

# set working diroctory "app" (just a convention, could be anything I like)
# inside the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure any bash script is executable
RUN chmod +x folders.sh
