# 🚀 Flask CRUD App with PostgreSQL (AWS RDS) & CI/CD on EC2

A simple **Flask CRUD (Create, Read, Update, Delete) web application** connected to a **PostgreSQL database hosted on AWS RDS**.  
Containerized with **Docker** and automatically deployed to an **Ubuntu EC2 instance** using **GitHub Actions CI/CD**.

---

## 📌 Features

- **Flask** web app with CRUD operations  
- **PostgreSQL** database hosted on AWS RDS  
- **Dockerized** for portability  
- **Automated CI/CD** pipeline with GitHub Actions  
- **Deployment** to AWS EC2 Ubuntu  

---

## ⚙️ Prerequisites

### 🟢 AWS Setup

- **EC2 Instance (Ubuntu)**
   - Docker installed
   - Security group inbound:
      - `22` (SSH)
      - `5000` (Flask app) or `80/443` (if using Nginx/SSL)
- **RDS PostgreSQL Instance**
   - Database + user created
   - Security group allows access from EC2 security group

### 🟢 GitHub Repository

Add **Secrets**:
- `DOCKER_PASSWORD` → Docker Hub password
- `SSH_USERNAME` → EC2 username (default: `ubuntu`)
- `PRIVATE_KEY` → Private SSH key for EC2 login
- `DB_PASS` → RDS database password

Add **Variables**:
- `DOCKER_USERNAME` → Your Docker Hub username
- `SSH_HOST` → EC2 Public IP or DNS
- `SSH_PORT` → 22
- `DB_HOST` → RDS endpoint
- `DB_NAME` → Database name
- `DB_USER` → Database username

---

## 🛠️ Local Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo>
```

---

### 2️⃣ Install Dependencies (for local run without Docker)

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Create Database Table in RDS

Login to your RDS PostgreSQL instance and run:

```sql
CREATE TABLE users (
   id SERIAL PRIMARY KEY,
   name VARCHAR(100),
   email VARCHAR(100)
);
```

---

### 4️⃣ Create `.env` File (optional for local testing)

```env
DB_HOST=<your-rds-endpoint>
DB_NAME=<your-db-name>
DB_USER=<your-db-username>
DB_PASS=<your-db-password>
```

---

### 5️⃣ Run Flask App Locally

```bash
python app.py
```

Open: [http://localhost:5000](http://localhost:5000)

---

### 🐳 Run with Docker

**Build Image:**
```bash
docker build -t flask-crud-app .
```

**Run Container:**
```bash
docker run -d -p 5000:5000 \
   --name flask-crud-app \
   -e DB_HOST=$DB_HOST \
   -e DB_NAME=$DB_NAME \
   -e DB_USER=$DB_USER \
   -e DB_PASS=$DB_PASS \
   flask-crud-app
```

Test: [http://localhost:5000](http://localhost:5000)

---

## 🔄 CI/CD with GitHub Actions

The CI/CD pipeline is defined in:  
`.github/workflows/deploy.yml`

### **Workflow Steps**

1. Checkout code
2. Login to Docker Hub
3. Build & push Docker image
4. SSH into EC2
5. Pull latest image & restart container

---


## ☁️ EC2 Setup (First Time)

On your Ubuntu EC2 instance:

```bash
# Update & install Docker
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# (Optional) Install docker-compose
sudo apt install -y docker-compose
```

Open security groups for:
- **Port 22** (SSH)
- **Port 5000** (Flask app)

---

## ✅ Testing the App

After deployment, visit:  
`http://<EC2-PUBLIC-IP>:5000`

### CRUD Operations

- **Add User** → Fill form & submit
- **Update User** → Edit fields & click update
- **Delete User** → Click delete button

**Quick Test via curl:**

```bash
# Check homepage
curl http://<EC2-PUBLIC-IP>:5000

# Add user (example)
curl -X POST -d "name=John&email=john@example.com" http://<EC2-PUBLIC-IP>:5000/add
```

---

## 📂 Project Structure

```
.
├── app.py                  # Flask application
├── templates/
│   └── index.html          # Frontend template
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container definition
└── .github/workflows/
      └── deploy.yml          # CI/CD pipeline
```

---

## 📖 Summary

This project demonstrates:

- Flask CRUD web app development
- PostgreSQL integration with AWS RDS
- Docker containerization
- CI/CD automation using GitHub Actions
- Deployment to Ubuntu EC2

> **Every push to `main` automatically builds, pushes, and deploys the app!**