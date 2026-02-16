"""
LogParser-AI Setup Configuration

Author: Ayi NEDJIMI
"""

from setuptools import setup, find_packages

setup(
    name="logparser_ai",
    version="1.0.0",
    author="Ayi NEDJIMI",
    author_email="contact@ayinedjimi-consultants.fr",
    description="Intelligent Log Parsing and Anomaly Detection",
    url="https://github.com/AYI-NEDJIMI/LogParser-AI",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    license="MIT",
)
