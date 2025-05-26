# Pytest Jenkins Integration Demo

This repository demonstrates how to integrate **Pytest** test automation with **Jenkins** CI/CD pipelines using a `Jenkinsfile`.

## 🔧 Project Purpose

The main goal of this project is to show:
- How to structure Pytest-based test automation
- How to run tests automatically using Jenkins pipelines
- How to configure Jenkins using a `Jenkinsfile`
- How to generate and visualize test reports (e.g., Allure)


## 🚀 How It Works

1. **Write tests** in the `test_scripts/` directory using Pytest.
2. **Commit to GitHub** — Jenkins is configured to poll or trigger builds on changes.
3. **Jenkinsfile** defines stages like:
   - Install dependencies
   - Run Pytest
   - Generate test reports (e.g., Allure)
4. **View test results** in Jenkins or via reports.

## 🧪 Requirements

- Python 3.x
- Pytest
- Jenkins (locally or on a CI server)
- Allure (optional, for rich test reporting)

Install dependencies:
```bash
pip install -r requirements.txt



