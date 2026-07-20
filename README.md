### 2. Django Web App

A web application built with Python and Django framework.

django-demo (Naturepro)

A Django web application, containerized with Docker and served via Gunicorn, deployed through a Jenkins CI/CD pipeline to Docker Hub and an EC2 host.

Naturepro is the core Django project inside this repo, with a testapp Django app providing the actual pages (index.html, info.html) served via templates.



Once deployed, the app is reachable at:

http://<host>:8000/


Tech stack
Language / Framework: Python, Django
WSGI server: Gunicorn (production-grade, replacing Django's dev server)
Containerization: Docker (single-stage, python:3.12-slim base)
CI/CD: Jenkins (declarative pipeline)
Registry: Docker Hub
Code quality: SonarQube (sonar-project.properties present for scan config)
Deployment target: AWS EC2



Project structure
django-demo/
├── Naturepro/                     # Django project package (settings, URLs, WSGI/ASGI entry points)
│   ├── __init__.py
│   ├── asgi.py                    # ASGI entry point (for async servers, e.g. Daphne/Uvicorn)
│   ├── wsgi.py                    # WSGI entry point — used by Gunicorn in production (Naturepro.wsgi:application)
│   ├── settings.py                # Django project settings
│   └── urls.py                    # Root URL routing
├── static/
│   ├── css/
│   └── images/
├── templates/testapp/
│   ├── index.html
│   └── info.html
├── testapp/                       # Django app providing the site's pages/views
├── venv/                          # Local virtual environment (not for production/containers)
├── Dockerfile                     # Container image definition (Gunicorn-based)
├── Jenkinsfile                    # CI/CD pipeline (build → push → deploy, Docker-based)
├── JenkinsfileD                   # Secondary/legacy pipeline definition (see note below)
├── manage.py                      # Django management CLI entry point
├── requirements.txt                # Python dependencies
├── sonar-project.properties       # SonarQube scanner configuration
├── db.sqlite3                     # SQLite database file
├── .gitignore
└── README.md