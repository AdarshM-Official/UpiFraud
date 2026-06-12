# UPI Fraud Detection System

A Django-based web application that leverages Machine Learning and Artificial Intelligence techniques to identify fraudulent UPI transactions and detect suspicious user activities in real time.

## Overview

The UPI Fraud Detection System is designed to enhance the security of digital payments by analyzing transaction patterns and identifying anomalies that may indicate fraudulent behavior. The system uses machine learning models to evaluate transaction data and classify transactions as legitimate or potentially fraudulent.

## Features

- User Registration and Authentication
- Secure Login System
- Real-Time Fraud Detection
- Anomaly Detection using Machine Learning
- Transaction Risk Analysis
- Fraud Probability Scoring
- User Dashboard
- Admin Dashboard
- Transaction Monitoring
- Fraud Alerts and Notifications
- Detailed Transaction History

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite3 | Database |
| Machine Learning | Fraud Detection |
| HTML/CSS | Frontend |
| JavaScript | Client-Side Interactivity |
| Tailwind CSS | UI Design |

## System Architecture

```text
User → Django Application → ML Model → Fraud Analysis
                     ↓
                 Database
                     ↓
              Admin Dashboard
```

## Project Structure

```text
UPIFRAUD/
│
├── accounts/          # Authentication and user management
├── core/              # Core application logic
├── templates/         # HTML templates
├── upifraud/          # Project settings and configuration
│
├── manage.py
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/upi-fraud-detection-system.git
cd upi-fraud-detection-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/
```

## Machine Learning Workflow

1. Collect Transaction Data
2. Preprocess and Clean Data
3. Feature Engineering
4. Train Machine Learning Model
5. Predict Fraud Probability
6. Generate Risk Score
7. Display Results to User/Admin

## Fraud Detection Parameters

The system analyzes:

- Transaction Amount
- Transaction Frequency
- Device Information
- Location Patterns
- Time of Transaction
- Beneficiary History
- User Behavioral Patterns
- Suspicious Activity Indicators

## Future Enhancements

- Real-Time UPI API Integration
- Deep Learning-Based Fraud Detection
- SMS and Email Alerts
- Geo-Location Tracking
- Explainable AI (XAI) Reports
- Dashboard Analytics and Visualizations
- Multi-Bank Integration

## Screenshots

Add project screenshots here.

### Home Page

```text
Insert Screenshot
```

### Fraud Detection Dashboard

```text
Insert Screenshot
```

### Admin Panel

```text
Insert Screenshot
```

## Contributors

- Adarsh M
- Nekha A
- Ajeesh Kumar B S

## License

This project is developed for educational and research purposes.

---

**UPI Fraud Detection System**
Detecting fraudulent transactions using Artificial Intelligence and Machine Learning.