# Detecting Data Leaks Using SQL Injection Protection

A secure cloud-based web application developed using **Python Flask**, **PostgreSQL**, and **AWS EC2** to prevent SQL Injection attacks, protect sensitive information using **AES-256 encryption**, and implement **Capability-Based Access Control (CBAC)** for secure database access.

---

# Project Overview

Data leakage is one of the major security threats in modern web applications. SQL Injection attacks can expose confidential information by executing unauthorized SQL queries. This project demonstrates a secure solution that prevents SQL Injection, encrypts sensitive data before storing it in the database, and restricts access based on user capabilities.

The application is deployed on **AWS EC2**, making it accessible over the internet while maintaining multiple layers of security.

---

# Objectives

* Detect and prevent SQL Injection attacks.
* Encrypt sensitive user information using AES-256.
* Implement Capability-Based Access Control (CBAC).
* Store encrypted data securely in PostgreSQL.
* Deploy the application on AWS EC2.
* Demonstrate secure cloud-based data storage.

---

# Features

* SQL Injection Detection
* AES-256 Data Encryption
* Secure PostgreSQL Database
* Capability-Based Access Control
* Flask Web Interface
* Cloud Deployment on AWS EC2
* Secure Database Queries
* Multi-layer Security
* Security Validation Report
* Encrypted Sensitive Data Storage

---

# Technology Stack

| Component            | Technology                      |
| -------------------- | ------------------------------- |
| Programming Language | Python 3                        |
| Framework            | Flask                           |
| Database             | PostgreSQL                      |
| Encryption           | Cryptography (Fernet - AES-256) |
| Cloud Platform       | AWS EC2                         |
| Frontend             | HTML                            |
| Database Driver      | psycopg2                        |
| Operating System     | Ubuntu Linux                    |

---

# Project Structure

```text
Sai_SQLI_Project/
│
├── app.py
├── database.py
├── encryption.py
├── access_control.py
├── validate_security.py
│
├── templates/
│     └── index.html
│
├── venv/
│
└── README.md
```


# System Architecture
```text


                    +----------------------+
                    |      End User        |
                    +----------+-----------+
                               |
                               |
                               v
                 +-----------------------------+
                 |      Flask Web Interface     |
                 |         (index.html)         |
                 +--------------+---------------+
                                |
                                |
                     Form Submission (POST)
                                |
                                v
                     +----------------------+
                     |      app.py          |
                     +----------+-----------+
                                |
               +----------------+----------------+
               |                                 |
               |                                 |
               v                                 v
+-----------------------------+      +------------------------------+
| SQL Injection Detection     |      | AES-256 Encryption Module    |
| Block Malicious Input       |      | encryption.py                |
+-------------+---------------+      +--------------+---------------+
              |                                     |
              +-------------------+-----------------+
                                  |
                                  v
                     +------------------------------+
                     | Capability Access Control    |
                     | access_control.py            |
                     +--------------+---------------+
                                    |
                                    v
                     +------------------------------+
                     | PostgreSQL Database          |
                     | users Table                 |
                     +--------------+---------------+
                                    |
                                    v
                     +------------------------------+
                     | Encrypted Data Storage       |
                     +--------------+---------------+
                                    |
                                    v
                     +------------------------------+
                     | Security Validation Report   |
                     | validate_security.py         |
                     +------------------------------+
```


# Workflow

1. User opens the Flask web application.
2. User enters Username, Sensitive Data, and Role.
3. SQL Injection patterns are checked.
4. Malicious input is rejected.
5. Sensitive information is encrypted using AES-256.
6. Capability-Based Access Control validates permissions.
7. Encrypted data is stored in PostgreSQL.
8. User receives a success confirmation.
9. Security validation confirms system integrity.

---

# Database Schema

## Database

securitydb


## Table

users


| Column      | Type               |
| ----------- | ------------------ |
| id          | SERIAL PRIMARY KEY |
| username    | VARCHAR(100)       |
| secret_data | TEXT               |
| role        | VARCHAR(20)        |



# Security Layers

### Layer 1

SQL Injection Protection

* Blocks malicious SQL keywords
* Prevents unauthorized SQL execution

### Layer 2

AES-256 Encryption

* Encrypts sensitive information before database storage
* Prevents plaintext data exposure

### Layer 3

Capability-Based Access Control

* Admin → Read & Write
* User → Read
* Auditor → View Logs

### Layer 4

Secure PostgreSQL Storage

* Uses parameterized SQL queries
* Prevents direct SQL manipulation

### Layer 5

Cloud Deployment

* Hosted securely on AWS EC2
* Accessible through Public IP


# SQL Injection Detection

Blocked keywords include:

DROP UNION SELECT

If detected, the application displays:

SQL Injection Detected


# Encryption Example

Input

Password123

Stored inside PostgreSQL

gAAAAABxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Sensitive information is never stored as plain text.


# Running the Project

Activate Virtual Environment

source venv/bin/activate

Run Flask Application

python3 app.py

Run Security Validation

python3 validate_security.py

# Testing

### Valid Input

Username
Sai

Sensitive Data
Password123

Role
Admin

#Result

Data Stored Successfully
AES-256 Encryption Enabled
SQL Injection Protection Enabled

#Author

**Venkata Saibabu Kalluri**
-Python | Flask | PostgreSQL | AWS EC2 | Cyber Security
-Detecting-Data-Leaks-Using-SQL-Injection-Protection
-Cloud Computing Internship Project

#License

This project is created for educational and academic purposes to demonstrate secure web application development techniques against SQL Injection attacks using encryption and cloud deployment.* Python Community
* Flask Framework
* PostgreSQL
* Cryptography Library
* AWS EC2
* Open Source Community
#Acknowledgements
Python Community
Flask Framework
PostgreSQL
Cryptography Library
AWS EC2
Open Source Community
