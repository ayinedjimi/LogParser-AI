# 📊 LogParser-AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/AYI-NEDJIMI)

[English](#english) | [Français](#français)

---

## English

### 🎯 Overview

**LogParser-AI** is an intelligent log parsing and anomaly detection system powered by Machine Learning. It automatically analyzes security logs, detects patterns, identifies anomalies, and provides actionable insights for Security Operations Centers (SOC).

### ✨ Key Features

- **🤖 ML-Powered Parsing**: Automatic log pattern extraction and classification
- **🚨 Anomaly Detection**: Real-time detection of unusual patterns and behaviors
- **📈 Pattern Recognition**: Identifies recurring patterns and baselines
- **🔍 Smart Filtering**: Intelligent noise reduction and event prioritization
- **⚡ High Performance**: Processes thousands of logs per second
- **🌐 Multi-Format Support**: Parse various log formats (Syslog, JSON, CEF, etc.)
- **📊 Visualization**: Built-in dashboards and analytics
- **🔗 REST API**: Easy integration with SIEM and other security tools
- **💾 Persistent Storage**: Store parsed logs and models
- **📝 Custom Rules**: Define custom parsing rules and anomaly patterns

### 🚀 Quick Start

#### Installation

```bash
# Clone the repository
git clone https://github.com/AYI-NEDJIMI/LogParser-AI.git
cd LogParser-AI

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

#### Basic Usage

```python
from logparser_ai import LogParser, AnomalyDetector

# Initialize parser
parser = LogParser()

# Parse logs
parsed_logs = parser.parse_file("access.log")

# Detect anomalies
detector = AnomalyDetector()
anomalies = detector.detect(parsed_logs)

for anomaly in anomalies:
    print(f"Anomaly: {anomaly.description}")
    print(f"Severity: {anomaly.severity}")
    print(f"Score: {anomaly.score}")
```

#### API Server

```bash
# Start the API server
python -m logparser_ai.api

# Upload and parse logs
curl -X POST "http://localhost:8000/parse" \
  -F "file=@access.log"

# Get anomalies
curl "http://localhost:8000/anomalies"
```

### 📋 Requirements

- Python 3.8+
- scikit-learn 1.3+
- FastAPI 0.104+
- 2GB+ RAM recommended

### 🏗️ Architecture

```
LogParser-AI/
├── src/
│   └── logparser_ai/
│       ├── __init__.py
│       ├── parser.py           # Log parsing engine
│       ├── detector.py         # Anomaly detection
│       ├── patterns.py         # Pattern extraction
│       ├── models.py           # ML models
│       ├── api.py              # FastAPI application
│       └── utils.py            # Utilities
├── models/                     # Pre-trained models
├── tests/
└── examples/
```

### 🔧 Configuration

Create a `config.yaml`:

```yaml
parser:
  formats:
    - syslog
    - json
    - cef
  batch_size: 1000

detector:
  algorithm: isolation_forest
  contamination: 0.1
  threshold: 0.8

storage:
  type: sqlite
  path: logs.db
```

### 📖 Supported Log Formats

- Syslog (RFC 3164, RFC 5424)
- JSON
- CEF (Common Event Format)
- Apache/Nginx Access Logs
- Windows Event Logs
- Custom formats via regex

### 🎓 Machine Learning Models

LogParser-AI uses multiple ML techniques:
- **Isolation Forest**: For anomaly detection
- **DBSCAN**: For clustering similar events
- **TF-IDF**: For text-based pattern matching
- **LSTM**: For time-series anomaly detection (optional)

### 📊 Anomaly Types Detected

- Unusual access patterns
- Failed authentication spikes
- Suspicious IP addresses
- Anomalous timestamps
- Rare error codes
- Deviation from baselines

### 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md).

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🔒 Security

For security concerns, please review our [Security Policy](SECURITY.md).

### 👤 Author

**Ayi NEDJIMI**

- Website: [ayinedjimi-consultants.fr](https://ayinedjimi-consultants.fr)
- HuggingFace: [@AYI-NEDJIMI](https://huggingface.co/AYI-NEDJIMI)
- LinkedIn: [Ayi NEDJIMI](https://linkedin.com/in/ayi-nedjimi)
- GitHub: [@AYI-NEDJIMI](https://github.com/AYI-NEDJIMI)

### 🔗 Related Projects

- [ThreatIntel-GPT](https://github.com/AYI-NEDJIMI/ThreatIntel-GPT) - AI threat intelligence analysis
- [SOC-Assistant](https://github.com/AYI-NEDJIMI/SOC-Assistant) - RAG-powered SOC assistant
- [IncidentSummarizer](https://github.com/AYI-NEDJIMI/IncidentSummarizer) - Incident ticket summarization
- [KVortex](https://github.com/AYI-NEDJIMI/kvortex) - Advanced RAG system

### 📚 Citation

```bibtex
@software{nedjimi2025logparser,
  author = {NEDJIMI, Ayi},
  title = {LogParser-AI: Intelligent Log Parsing and Anomaly Detection},
  year = {2025},
  url = {https://github.com/AYI-NEDJIMI/LogParser-AI}
}
```

---

## Français

### 🎯 Aperçu

**LogParser-AI** est un système intelligent d'analyse de logs et de détection d'anomalies alimenté par le Machine Learning. Il analyse automatiquement les journaux de sécurité, détecte les patterns, identifie les anomalies et fournit des informations exploitables pour les SOC.

### ✨ Fonctionnalités Clés

- **🤖 Parsing ML**: Extraction et classification automatique des patterns de logs
- **🚨 Détection d'Anomalies**: Détection en temps réel de patterns et comportements inhabituels
- **📈 Reconnaissance de Patterns**: Identification des patterns récurrents et baselines
- **🔍 Filtrage Intelligent**: Réduction de bruit et priorisation d'événements
- **⚡ Haute Performance**: Traitement de milliers de logs par seconde
- **🌐 Multi-Format**: Parse divers formats (Syslog, JSON, CEF, etc.)
- **📊 Visualisation**: Tableaux de bord et analytics intégrés
- **🔗 API REST**: Intégration facile avec SIEM et autres outils

### 🚀 Démarrage Rapide

#### Installation

```bash
# Cloner le dépôt
git clone https://github.com/AYI-NEDJIMI/LogParser-AI.git
cd LogParser-AI

# Installer les dépendances
pip install -r requirements.txt

# Installer le package
pip install -e .
```

### 👤 Auteur

**Ayi NEDJIMI**

- Site Web: [ayinedjimi-consultants.fr](https://ayinedjimi-consultants.fr)
- HuggingFace: [@AYI-NEDJIMI](https://huggingface.co/AYI-NEDJIMI)
- LinkedIn: [Ayi NEDJIMI](https://linkedin.com/in/ayi-nedjimi)
- GitHub: [@AYI-NEDJIMI](https://github.com/AYI-NEDJIMI)

---

**Made with ❤️ for cybersecurity professionals**
