# {{cookiecutter.project_slug}}/Makefile

.PHONY: help requirements clean docker-build docker-run run-api

# Infer project slug from the directory name containing the Makefile
# This makes the Makefile work correctly when run from the generated project root
PROJECT_SLUG := $(shell basename $(CURDIR))

help:
	@echo "Available commands:"
	@echo "  requirements   Install project dependencies from requirements.txt"
	@echo "  clean          Remove temporary files"
	@echo "  docker-build   Build the Docker image (tagged as $(PROJECT_SLUG))"
	@echo "  docker-run     Run the Docker container (example: interactive shell)"
	@echo "  run-api        Run the FastAPI development server (requires fastapi/uvicorn installed)"

requirements:
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "Dependencies installed from requirements.txt."

# Removed lint target
# lint:
#	ruff check .
#	ruff format --check .
#	@echo "Linting checks passed."

# Removed test target
# test:
#	pytest tests/
#	@echo "Tests passed."

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache .coverage htmlcov build dist *.egg-info mlruns
	@echo "Temporary files cleaned."

# Docker commands
IMAGE_NAME := $(PROJECT_SLUG)

docker-build:
	@echo "Building Docker image: $(IMAGE_NAME)..."
	docker build -t $(IMAGE_NAME) .
	@echo "Docker image $(IMAGE_NAME) built."

docker-run:
	@echo "Running Docker container $(IMAGE_NAME) interactively..."
	docker run -it --rm -v "${PWD}":/app $(IMAGE_NAME) bash
	@echo "Exited Docker container."

# Example command to run the API using uvicorn
run-api:
	uvicorn src.$(PROJECT_SLUG).api.main:app --host 0.0.0.0 --port 8000 --reload

# Add other commands like 'train', 'predict' as needed
# Example:
# train:
#	 python src/$(PROJECT_SLUG)/models/train_model.py

