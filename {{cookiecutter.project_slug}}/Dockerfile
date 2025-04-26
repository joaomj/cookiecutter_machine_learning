# {{cookiecutter.project_slug}}/Dockerfile

# Use an official Python runtime as a parent image
# Using a slim image reduces size but might lack some build tools if compilation is needed.
FROM python:{{ cookiecutter.python_version }}-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1      # Prevents Python from buffering stdout and stderr

# Set the working directory in the container
WORKDIR /app

# Install system dependencies if needed (e.g., for specific Python packages)
# Some Python packages (e.g., geospatial, some ML/optimization) might require system libraries.
# If pip install fails or takes too long compiling, uncomment and add necessary packages.
# Example: Install build-essential for C/C++ compilation
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# Copy only requirements first to leverage Docker layer caching.
COPY requirements.txt .
# Use --no-cache-dir to reduce image size.
# Pip prioritizes pre-compiled wheels (.whl) over source distributions (.tar.gz),
# which minimizes compilation time for common packages on standard architectures.
# If builds are slow due to compilation, check if wheels are available for your specific
# dependencies and platform, or if required system build tools are missing (see above).
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Create a non-root user and group for security
RUN addgroup --system app && adduser --system --ingroup app app

# Copy the rest of the application code into the container
# Ensure .dockerignore is properly configured to exclude unnecessary files
COPY . .

# Change ownership of the app directory to the non-root user
RUN chown -R app:app /app

# Switch to the non-root user
USER app

# Expose port if the application is a web service (e.g., FastAPI)
# Adjust the port number based on your application (e.g., 8000 for FastAPI default)
EXPOSE 8000

# Define the command to run your application
# This is just an example for running a FastAPI app using uvicorn.
# Change this to run a training script, prediction script, batch job, etc.
# Or leave it empty and specify the command during `docker run`.
CMD ["uvicorn", "src.{{cookiecutter.project_slug}}.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
