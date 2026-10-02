# Task 11: Full Application Containerization

## CIFAR-10 Deep Learning Application

A Dockerized image classification application integrating a TensorFlow CNN, Flask REST API, and Streamlit user interface.

## Features

* Deep learning image classification
* Flask REST API
* Streamlit user interface
* Docker image creation
* Docker Compose integration
* Health monitoring
* JSON prediction responses

## Technology Stack

* Python
* TensorFlow
* Flask
* Streamlit
* Docker
* Docker Compose

## Project Structure

```text
Task11_Full_Application_Containerization/
├── model/
│   └── train_model.py
├── api/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── cifar10_model.keras
├── ui/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── tests/
│   └── test_api.py
├── screenshots/
├── reports/
├── docs/
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

## Execution

Build the application:

```powershell
docker compose build
```

Start:

```powershell
docker compose up -d
```

Check status:

```powershell
docker compose ps
```

Open the interface:

http://localhost:8501

API:

http://localhost:5000

Stop:

```powershell
docker compose down
```

## Author

Sharon Thoppil

## Academic Task

L&T Edutech – Task 11: Full Application Containerization
