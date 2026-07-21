# 🚀 DevOps Control Center (DCC)

> A Production-Ready Self-Hosted DevOps Platform built with FastAPI, PostgreSQL, Docker, Terraform, Ansible, Jenkins and Kubernetes.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Terraform](https://img.shields.io/badge/Terraform-IaC-623CE4)
![Ansible](https://img.shields.io/badge/Ansible-Automation-red)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-orange)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5)

---

# 📖 Overview

DevOps Control Center (DCC) is a centralized DevOps platform that enables engineers to manage projects, infrastructure, deployments, and servers from a single dashboard.

Instead of manually logging into servers and executing commands, DCC automates deployment workflows using Docker, Terraform, Ansible, Jenkins, and Kubernetes.

The goal of this project is to simulate a lightweight version of modern DevOps platforms like:

- Render
- Railway
- Portainer
- Terraform Cloud
- Jenkins
- Rancher

---

# ✨ Features

## Authentication

- JWT Authentication
- Secure Password Hashing (bcrypt)
- User Registration
- Login
- Protected APIs

---

## Project Management

- Create Projects
- Manage Multiple Projects
- User-based Ownership
- Deployment History

---

## Server Management

- Register Remote Servers
- SSH Connectivity
- Server Status
- Secure Credentials

---

## Docker Deployment

- Clone Git Repository
- Build Docker Images
- Run Containers
- Restart Containers
- Remove Containers
- View Logs

---

## Terraform Integration

Provision Infrastructure directly from the dashboard.

Supported Operations:

- terraform init
- terraform plan
- terraform apply
- terraform destroy

---

## Ansible Automation

Execute playbooks remotely.

Examples:

- Install Docker
- Install Nginx
- Configure Server
- Deploy Applications

---

## Jenkins Integration

Complete CI/CD Pipeline

GitHub Push

↓

Jenkins Build

↓

Docker Image

↓

Deploy to Server

↓

Deployment Status

---

## Kubernetes

Deploy applications directly into Kubernetes.

Future Features

- Deployments
- Services
- Scaling
- Rollback
- Pods Monitoring

---

## Monitoring

- CPU Usage
- RAM Usage
- Disk Usage
- Docker Containers
- Deployment Logs
- Server Health

---

# 🏗 Architecture

```

                 GitHub Repository
                        │
                        ▼
                 Jenkins Pipeline
                        │
                        ▼
                  Docker Build
                        │
                        ▼
              DevOps Control Center
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Terraform          Ansible          Kubernetes
      │                 │                 │
      ▼                 ▼                 ▼
 AWS EC2          Server Config      Deploy Apps

```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- Passlib

## Database

- PostgreSQL

## DevOps

- Docker
- Docker Compose
- Terraform
- Ansible
- Jenkins
- Kubernetes

## Cloud

- AWS EC2

## Authentication

- JWT
- OAuth2

---

# 📂 Project Structure

```

DevOps-Control-Center

│

├── app/

│ ├── models/

│ ├── schemas.py

│ ├── crud.py

│ ├── security.py

│ ├── database.py

│ ├── config.py

│ └── main.py

│

├── terraform/

├── ansible/

├── docker/

├── kubernetes/

├── jenkins/

├── scripts/

├── requirements.txt

└── README.md

```

---

# 🔐 Authentication Flow

```

Register

↓

Login

↓

JWT Token

↓

Authorization Header

↓

Protected APIs

↓

Deploy Infrastructure

```

---

# 🚀 API Endpoints

## Authentication

| Method | Endpoint | Description |
|----------|----------------|---------------------|
| POST | /register | Register User |
| POST | /login | Login User |
| GET | /me | Current User |

---

## Projects

| Method | Endpoint |
|----------|----------------|
| POST | /projects |
| GET | /projects |
| DELETE | /projects/{id} |

---

## Servers

| Method | Endpoint |
|----------|---------------|
| POST | /servers |
| GET | /servers |
| DELETE | /servers/{id} |

---

## Deployments

| Method | Endpoint |
|----------|---------------------|
| POST | /deploy |
| GET | /deployments |
| GET | /logs |

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/devops-control-center.git

cd devops-control-center
```

Create Virtual Environment

```bash
python -m venv myenv
```

Activate

Windows

```bash
myenv\Scripts\activate
```

Linux

```bash
source myenv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment

Create `.env`

```env
DATABASE_URL=postgresql://username:password@localhost/dcc_db

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

Run

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# Current Progress

| Module | Status |
|---------|--------|
| Authentication | ✅ |
| PostgreSQL | ✅ |
| JWT | ✅ |
| Projects | ✅ |
| Server Management | 🚧 |
| Docker Deployment | ⏳ |
| Terraform | ⏳ |
| Jenkins | ⏳ |
| Ansible | ⏳ |
| Kubernetes | ⏳ |
| Monitoring | ⏳ |

---

# Future Roadmap

- Live Deployment Logs
- GitHub Integration
- Docker Registry
- Multi-user Support
- RBAC
- Notifications
- Kubernetes Dashboard
- Metrics
- Prometheus
- Grafana
- AWS Auto Scaling

---

# 🎯 Why this Project?

This project demonstrates practical implementation of modern DevOps practices by combining Infrastructure as Code (Terraform), Configuration Management (Ansible), Containerization (Docker), Continuous Integration/Deployment (Jenkins), Container Orchestration (Kubernetes), and Cloud Infrastructure (AWS) into a single centralized platform.

---

# 👨‍💻 Author

**Krishna Jaiswal**

B.Tech AI & Data Science

DevOps | DevSecOps | Cloud | Automation

---

⭐ If you like this project, don't forget to star the repository. 
