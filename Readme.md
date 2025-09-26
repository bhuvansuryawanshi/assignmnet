# 🚀 Python App with Docker & GitHub Actions CI/CD

This repository contains a **Python application** deployed on an **AWS EC2 instance** using **Docker** and automated with **GitHub Actions**.

---

## 📌 Project Workflow

1. **Database Setup**
   - Create a PostgreSQL/MySQL database (choose based on app).
   - Note the following details:
     - `DB_HOST`
     - `DB_NAME`
     - `DB_USER`
     - `DB_PASS`
   - Add these values to **GitHub Repository → Settings → Secrets and Variables → Actions**.

   Example (PostgreSQL):
   ```sql
   CREATE DATABASE mydb;
   CREATE USER myuser WITH PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

```
   CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT 
    CURRENT_TIMESTAMP
    );
```

## ☁️ EC2 Instance Setup

1. **Launch an Ubuntu EC2 Instance**
   - Go to AWS Console → EC2 → Launch Instance
   - Choose **Ubuntu 22.04 LTS**
   - Select appropriate instance type (e.g., `t2.micro` for testing)
   - Configure key pair (download `.pem` file)
   - Configure security group (open required ports)

---

2. **Install Docker**
   SSH into your EC2 instance:
   ```bash
   ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
