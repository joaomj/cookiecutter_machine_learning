# Cookiecutter Machine Learning Project Template

A Cookiecutter template for creating lean Machine Learning projects with Python, including Docker support and a basic structure for data processing, modeling, and API deployment.

## Features

* **Standardized Structure:** Provides a well-defined directory layout for ML projects (`data/`, `src/`, `notebooks/`, `configs/`, `outputs/`).
* **Python Package Ready:** Source code organized within `src/{{cookiecutter.project_slug}}/` making it installable.
* **Docker Integration:** Includes a basic `Dockerfile` and `.dockerignore` for containerizing the project.
* **Configuration Management:** A `configs/` directory with an example `params.yaml`.
* **API Placeholder:** Basic structure for deploying models via a FastAPI API (`src/api/`).
* **Makefile:** Includes basic commands for common tasks (installing requirements, building Docker image, etc.).
* **GitHub Ready:** Includes a `.github/CODEOWNERS` file.
* **User Specific Folders:** Includes placeholders for `.clinerules` and `memory-bank/` (ignored by default in generated projects).
* **Minimal Dependencies:** Starts with a commented-out `requirements.txt`, allowing users to define their exact needs.

## Usage

First, make sure you have Cookiecutter installed:

```bash
pip install cookiecutter
# or using pipx (recommended)
pipx install cookiecutter
# or using uv
uv pip install cookiecutter
To generate a new project using this template:cookiecutter gh:joaomj/cookiecutter_machine_learning
Or, if you have cloned the template locally:cookiecutter /path/to/cookiecutter_machine_learning
Cookiecutter will prompt you for the following values:project_name: The human-readable name of your project.project_slug: The name for the project directory and Python package (auto-generated from project_name).author_name: Your name.author_email: Your email address.github_username: Your GitHub username (used for CODEOWNERS and LICENSE).description: A short description of the project.python_version: The target Python version (e.g., 3.12).license: The license for the generated project (default: MIT).year: The copyright year (auto-generated).Generated Project Structure{{cookiecutter.project_slug}}/
├── .github/            <- GitHub related files (e.g., CODEOWNERS)
├── .gitignore          <- Files ignored by Git
├── .dockerignore       <- Files ignored by Docker build context
├── .clinerules         <- Cline rules file (user-specific)
├── Dockerfile          <- Docker configuration for the project
├── LICENSE             <- Project license ({{ cookiecutter.license }})
├── Makefile            <- (Optional) Shortcuts for common commands
├── README.md           <- Project-specific README
├── configs/            <- Configuration files (e.g., params.yaml)
├── data/               <- Project data (raw, processed)
│   ├── processed/
│   └── raw/
├── memory-bank/        <- User-specific memory bank directory
├── notebooks/          <- Jupyter notebooks for exploration
├── outputs/            <- Generated outputs (figures, reports, etc.)
├── requirements.txt    <- Project dependencies (initially commented out)
└── src/{{cookiecutter.project_slug}}/ <- Source code package
    ├── __init__.py
    ├── data/           <- Data processing scripts
    ├── features/       <- Feature engineering scripts
    ├── models/         <- Model training and prediction scripts
    └── api/            <- API related code (e.g.,
