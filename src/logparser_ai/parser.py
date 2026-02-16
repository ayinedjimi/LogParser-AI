"""
Log Parser with ML-based pattern extraction

Author: Ayi NEDJIMI
"""

import re
import json
from typing import List, Dict, Any
from datetime import datetime


class LogParser:
    """Intelligent log parsing engine"""

    def __init__(self):
        self.patterns = {
            'syslog': r'^(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+)\s+(\S+):\s+(.*)',
            'apache': r'^(\S+)\s+\S+\s+\S+\s+\[(.*?)\]\s+"(\S+)\s+(\S+)\s+(\S+)"\s+(\d+)\s+(\S+)',
            'json': None  # JSON parsed differently
        }

    def parse_file(self, filepath: str, format: str = 'auto') -> List[Dict[str, Any]]:
        """Parse log file"""
        with open(filepath, 'r') as f:
            lines = f.readlines()
        return self.parse_lines(lines, format)

    def parse_lines(self, lines: List[str], format: str = 'auto') -> List[Dict[str, Any]]:
        """Parse log lines"""
        parsed = []
        for line in lines:
            try:
                if format == 'json' or (format == 'auto' and line.strip().startswith('{')):
                    parsed.append(json.loads(line))
                else:
                    parsed.append(self._parse_text_line(line, format))
            except:
                continue
        return parsed

    def _parse_text_line(self, line: str, format: str) -> Dict[str, Any]:
        """Parse text log line"""
        if format == 'syslog' or format == 'auto':
            match = re.match(self.patterns['syslog'], line)
            if match:
                return {
                    'timestamp': match.group(1),
                    'hostname': match.group(2),
                    'service': match.group(3),
                    'message': match.group(4)
                }
        return {'raw': line.strip()}
