# ☁️ CloudPulse Sentinel

### AWS-Powered API Testing & Monitoring Framework

CloudPulse Sentinel is a cloud-native API testing and real-time monitoring framework built with Python, pytest, and AWS. It automatically tests REST API endpoints, monitors their health, stores reports in S3, and triggers SNS alerts when failures are detected — all powered by a CI/CD pipeline via GitHub Actions.

---

## 🚀 Features

- ✅ Automated REST API testing — GET, POST, PUT, DELETE, Headers, Health checks
- ☁️ AWS Lambda for serverless API health monitoring
- 📦 S3 integration for automatic test report storage
- 🔔 SNS real-time alerting on API failures
- 🔄 CI/CD pipeline with GitHub Actions (runs on every push)
- 🧪 Schema validation using JSON Schema
- 📋 Structured logging for traceability

---

## 🗂️ Project Structure

```
CloudPulse-Sentinel/
├── .github/
│   └── workflows/
│       └── api-tests.yml        # GitHub Actions CI/CD pipeline
├── aws/
│   ├── lambda_function.py       # AWS Lambda health monitor + SNS alerts
│   └── s3_upload.py             # S3 report upload logic
├── config/
│   └── endpoints.json           # API base URLs and endpoints
├── schemas/
│   └── user_schema.json         # JSON schema for response validation
├── tests/
│   ├── test_delete_api.py       # DELETE request tests
│   ├── test_headers_api.py      # Headers validation tests
│   ├── test_health_api.py       # Health check tests
│   ├── test_post_api.py         # POST request tests
│   └── test_put_api.py          # PUT request tests
├── utils/
│   ├── __init__.py
│   └── api_client.py            # Reusable API request functions
├── logger.py                    # Centralized logging setup
├── pytest.ini                   # Pytest configuration
└── requirements.txt             # Project dependencies
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Testing Framework | pytest |
| HTTP Client | requests |
| Cloud Provider | AWS (Lambda, S3, SNS) |
| CI/CD | GitHub Actions |
| Schema Validation | jsonschema |
| Reporting | pytest-html |

---

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/jahnavi-gummalla/CloudPulse-Sentinel.git
cd CloudPulse-Sentinel
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
```
BUCKET_NAME=your-s3-bucket-name
TOPIC_ARN=your-sns-topic-arn
```

---

## ▶️ Running Tests

```bash
# Run all tests
pytest

# Run with HTML report
pytest --html=reports/report.html

# Run a specific test file
pytest tests/test_health_api.py
```

---

## ☁️ AWS Architecture

```
GitHub Actions (CI/CD)
        ↓
   pytest runs all API tests
        ↓
AWS Lambda triggered on schedule
        ↓
   API Health Check
   ├── ✅ Success → Upload report to S3
   └── ❌ Failure → Trigger SNS Alert → Email/Notification
```

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch automatically:
1. Sets up Python 3.11 environment
2. Installs all dependencies
3. Runs the full pytest test suite

Configured in `.github/workflows/api-tests.yml`

---

## 📊 Test Coverage

| Test File | Methods Tested |
|---|---|
| test_health_api.py | GET — Health check |
| test_post_api.py | POST — Create resource |
| test_put_api.py | PUT — Update resource |
| test_delete_api.py | DELETE — Remove resource |
| test_headers_api.py | Headers — Validation |

---

## 👩‍💻 Author

**Jahnavi Gummalla**
[GitHub](https://github.com/jahnavi-gummalla)

---

> *CloudPulse Sentinel — Continuously watching. Instantly alerting. Always reliable.*
