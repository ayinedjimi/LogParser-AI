"""
Anomaly Detector using Machine Learning

Author: Ayi NEDJIMI
"""

from sklearn.ensemble import IsolationForest
from typing import List, Dict, Any
import numpy as np


class AnomalyDetector:
    """ML-based anomaly detection"""

    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.trained = False

    def train(self, logs: List[Dict[str, Any]]):
        """Train anomaly detection model"""
        features = self._extract_features(logs)
        self.model.fit(features)
        self.trained = True

    def detect(self, logs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect anomalies in logs"""
        if not self.trained:
            self.train(logs)

        features = self._extract_features(logs)
        predictions = self.model.predict(features)
        scores = self.model.score_samples(features)

        anomalies = []
        for i, (pred, score) in enumerate(zip(predictions, scores)):
            if pred == -1:  # Anomaly
                anomalies.append({
                    'log': logs[i],
                    'score': float(score),
                    'severity': self._get_severity(score)
                })
        return anomalies

    def _extract_features(self, logs: List[Dict[str, Any]]) -> np.ndarray:
        """Extract numerical features from logs"""
        features = []
        for log in logs:
            # Simple feature extraction - enhance for production
            f = [
                len(str(log.get('message', ''))),
                len(log.keys()),
                hash(str(log.get('service', ''))) % 1000
            ]
            features.append(f)
        return np.array(features)

    def _get_severity(self, score: float) -> str:
        """Convert anomaly score to severity"""
        if score < -0.5:
            return "CRITICAL"
        elif score < -0.3:
            return "HIGH"
        elif score < -0.1:
            return "MEDIUM"
        return "LOW"
