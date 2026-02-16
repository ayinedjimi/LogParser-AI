"""
Pattern Extractor for log analysis

Author: Ayi NEDJIMI
"""

from collections import Counter
from typing import List, Dict, Any


class PatternExtractor:
    """Extract common patterns from logs"""

    def extract(self, logs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract patterns from logs"""
        services = Counter()
        errors = []
        timestamps = []

        for log in logs:
            if 'service' in log:
                services[log['service']] += 1
            if 'error' in str(log).lower():
                errors.append(log)
            if 'timestamp' in log:
                timestamps.append(log['timestamp'])

        return {
            'total_logs': len(logs),
            'top_services': services.most_common(10),
            'error_count': len(errors),
            'time_range': {
                'start': min(timestamps) if timestamps else None,
                'end': max(timestamps) if timestamps else None
            }
        }
