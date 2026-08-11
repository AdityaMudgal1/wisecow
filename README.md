# Wisecow – Kubernetes Deployment with Docker, CI/CD and TLS

Wisecow is a simple web application that displays random cow wisdom.
This project containerizes the application using Docker and deploys it on
Kubernetes with a Kubernetes Service, NGINX Ingress, HTTPS/TLS, and GitHub Actions.

---

## Problem Statement

Deploy the Wisecow application as a Kubernetes application.

### Requirements

1. Create a Dockerfile and corresponding Kubernetes manifests to deploy the
   Wisecow application in a Kubernetes environment. The Wisecow service should
   be exposed using a Kubernetes Service.

2. Create a GitHub Actions workflow to build a new Docker image when changes
   are made to the repository.

3. Challenge Goal: Enable secure TLS communication for the Wisecow application.

---

## Technologies Used

- Docker
- Kubernetes
- Minikube
- NGINX Ingress Controller
- GitHub Actions
- GitHub Container Registry (GHCR)
- TLS / HTTPS
- Ubuntu 24.04

---

## Project Structure

```text
wisecow/
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── .gitignore
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── ingress.yaml
├── wisecow.sh
├── README.md
└── LICENSE