# Flask Movie API

A scalable and powerful **RESTful API** built with **Flask**, designed for efficient management of a movie and actor database.

The application demonstrates advanced architectural approaches: strict dependency isolation, database migrations, web scraping integration, containerization, automated testing, and comparative analysis of multithreading vs multiprocessing for performance optimization.

The application ensures fast integration, easy scalability, and high data security.

## 📊 Status of Workflows

[![Tests in Docker](https://github.com/OleksiiChudovskyi/flask_movie/actions/workflows/tests_docker.yml/badge.svg?branch=main)](https://github.com/OleksiiChudovskyi/flask_movie/actions/)
[![Tests in VM](https://github.com/OleksiiChudovskyi/flask_movie/actions/workflows/tests_vm.yml/badge.svg?branch=main)](https://github.com/OleksiiChudovskyi/flask_movie/actions/)

---

## 🌐 Live Demo (Production)

The project is deployed and running in a production environment on Railway. You can explore the interactive documentation and test the API at:
👉 **[Production version Flask Movie API](https://movie-flask.up.railway.app/api/v1/swagger/)**

## 🚀 Project Features

* **Modern Stack**: Built on Python 3.11 and Flask.
* **RESTful Architecture**: Full compliance with REST principles, using Flask-RESTful and Marshmallow for clean data serialization and request validation.
* **Data Management**: Full-featured ORM SQLAlchemy (PostgreSQL) and automatic migrations via Flask-Migrate (Alembic).
* **Web Scraping Module**: Integrated IMDb scraper using BeautifulSoup4 and Requests to automatically populate the database with up-to-date information.
* **Concurrency & Optimization**: Three different strategies implemented for demonstrating optimization of I/O-bound operations.
* **Environment Isolation**: Separate Docker configurations for development, testing, and stable production.
* **Security**: JWT token generation and validation (PyJWT), plus password protection via Docker Secrets.
* **Documentation**: Integrated Swagger UI for real-time endpoint testing.
* **Quality Control**: Test coverage (Pytest, Coverage, Mock) and automated style checks (Flake8).
* **Code Quality & CI/CD:** Automated workflows via GitHub Actions, including testing, linting, and formatting with `Ruff`.

## 🛠️ Tech Stack

* **Language**: Python 3.11+
* **Framework**: Flask, Flask-RESTful
* **Validation**: Marshmallow
* **Database & ORM**: PostgreSQL, Flask-SQLAlchemy, Flask-Migrate, Alembic
* **Package Manager**: Poetry
* **Security & Tools**: PyJWT, BeautifulSoup4 (bs4), Requests
* **WSGI & Server**: Gunicorn, NGINX
* **DevOps**: Docker, Docker Compose

## 🏎️ Scraping Module & Concurrency Strategies

The project includes a tool for automatically populating the database with top movies from IMDb. Three approaches are implemented to study network request performance:

1. **Synchronous Parsing (`PopulateDB`)**: Sequential data collection for each movie. Slowest option due to I/O blocking.
2. **Multithreaded Parsing (`PopulateDBThreaded`)**: Uses Python’s `threading` module. Multiple requests run in parallel, significantly speeding up data collection by switching during I/O waits.
3. **Process Pool (`PopulateDBThreadPoolExecutor`)**: Uses `ProcessPoolExecutor` (with option to switch to `ThreadPoolExecutor`), distributing tasks across OS processes for HTML parsing.

---

## 📝 Repository Version & Code Transparency

This repository was created to transparently demonstrate project architecture and development skills.

- **Full Source Code:** The [Flask Movie API GitHub repository](https://github.com/OleksiiChudovskyi/flask_movie) contains the complete source code, architecture, and configuration files/folders typically excluded via `.gitignore` and `.dockerignore`.  
  This was done intentionally so you can explore the full development cycle.
- **Data Security:** To prevent leaks of sensitive information (private API keys, authentication tokens, database passwords), the commit history was fully reset.  
  Current configuration files contain only safe demo values.

## 📦 Installation and configuration locally

Make sure you have **Python 3.11** and **Poetry** installed.

1. Clone the repository:
```bash
git clone https://github.com/OleksiiChudovskyi/flask_movie.git
cd flask_movie
```

2. Install dependencies via Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

----

## 📦 Containerization and Environments

The project has several Docker Compose configurations adapted to different usage scenarios:

1. **Development:** Supports `docker compose watch` technology for real-time Hot Reloading of code without rebuilding images.
2. **Testing:** Separate isolated test execution based on `Pytest` and calculation of code coverage using `Coverage`.
3. **Production:** Maximum security version using Docker Secrets, optimized images and **NGINX** reverse proxy.

## 🐳 Launch via Docker Compose

Make sure you have Git and Docker installed on your computer
(with Docker Compose v2.22.0+ to support watch mode).

The project supports three out-of-the-box Docker scripts for different stages of development:

### 1. Development
Uses the `Deploy and watch` mechanism to instantly update containers while editing code:
```bash
docker compose -f compose.dev.yml up --build --watch
```

### 2. Testing
Runs tests inside a container via `Pytest`, using the fast `sqlite3:memory:` database, and automatically generates a `coverage` report:
```bash
docker compose -f compose.test.yml up --build
```

### 3. Production
Launches a load-tolerant architecture.
The application runs through `Gunicorn`, requests are proxied through `NGINX`,
and passwords and keys are securely protected using `Docker Secrets`:

Before running Docker Compose, be sure to export environment variables to the current terminal session using the installation script:
```bash
source ./sets/set_env.sh
```

Run containers in the background (detached mode).
The automatic image build process is optimized for minimum size and maximum security:
```bash
docker compose -f compose.prod.yml up -d --build
```
**When starting containers, the following will automatically happen:**
1. Waiting for the PostgreSQL database to be ready.
2. Automatic application of all Alembic migrations.
3. Automatic seeding of the database with initial/test data (Seeding).

---

## 📈 Testing and Code Quality

To run tests locally (without Docker), use the following commands:

```bash
# Run tests and analyze code coverage
poetry run pytest --cov=src

# Check code for PEP 8 compliance
poetry run flake8 src
```
### CI/CD Workflow (GitHub Actions)
Two automated scripts (Workflows) are configured in the repository:
1. **Docker Compose Tests:** Runs a test container on each Pull Request / Push to verify the integrity of the infrastructure.
2. **Comprehensive Code Check:** Runs on a GitHub Runner virtual machine and performs:
- Testing (Pytest).
- Static analysis and linting (`Ruff Check`).
- Code formatting check (`Ruff Format`).

---

## 🗺️ API Endpoints Overview

After the project is launched, the interactive documentation of **Swagger UI** is available at: `http://localhost:8001/api/v1/swagger/`.

### 🔐 Authentication and Security
* `POST /register` — Register a new user of the system (`AuthRegister`).
* `POST /login` — Authorize the user and obtain a JWT access token (`AuthLogin`).

### 📊 Analytics and Data Aggregation
* `GET /aggregations` — Obtain summary and analytical information about movies and actors (`AggregationApi`).

### 🤖 Automatic database filling (IMDb Scraper)
* `POST /populate_db` — Populate the database using the synchronous method (`PopulateDB`).
* `POST /populate_db_threaded` — Populate the database using `threading` threads (`PopulateDBThreaded`).
* `POST /populate_db_executor` — Populate the database using a thread pool (`PopulateDBThreadPoolExecutor`).

### 🎬 Films
* `GET /films` — Get a list of all movies.
* `POST /films` — Add a new movie.
* `GET /films/{uuid}` — Get details of a specific movie.
* `PUT /films/{uuid}` — Update information about a movie.
* `PATCH /films/{uuid}` — Update information about a movie.
* `DELETE /films/{uuid}` — Delete a movie.

### 🎭 Actors
* `GET /actors` — Get a list of all actors.
* `POST /actors` — Add a new actor.
* `GET /actors/{uuid}` — Get details of a specific actor.
* `PUT /actors/{uuid}` — Update information about an actor.
* `PATCH /actors/{uuid}` — Update actor information.
* `DELETE /actors/{uuid}` — Delete actor.

---

## 📝 License

This project is open source and distributed under the [MIT License](LICENSE).

## 👥 Author

**Oleksii Chudovskyi** — [oleksii.chudovskyi@gmail.com](mailto:oleksii.chudovskyi@gmail.com)