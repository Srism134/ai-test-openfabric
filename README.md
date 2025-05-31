# ai-test-openfabric
# 🧠 Openfabric AI App – Local Chatbot with SQLite

This is a local AI app powered by [Openfabric.ai](https://openfabric.ai), running a custom chatbot model with SQLite database integration.

---

## 📦 Features

- ✅ Runs fully **locally** without internet
- ✅ Built using `openfabric-pysdk`
- ✅ Uses a **pre-defined ontology**
- ✅ SQLite database integration (included)
- ✅ Ready to deploy or test locally

---

## 🛠️ Tech Stack

- Python 3.10+
- `openfabric-pysdk==0.2.9`
- `Flask`, `Flask-RESTful`, `marshmallow==3.19.0`
- SQLite

---

## 🚀 How to Run Locally

### 1. Clone the Repo
```bash

cd ai-test-openfabric
### 📂 Project Structure
ai-test-openfabric/
├── app/
│   ├── main.py
│   ├── ontology_dc8f06af066e4a7880a5938933236037/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── input.py
│   │   ├── output.py
│   │   └── brain.py
├── database/
│   └── chatbot.db
├── requirements.txt
├── pyproject.toml
└── README.md

