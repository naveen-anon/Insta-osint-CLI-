# tests/test_analyzers.py
import unittest
from analyzers.timeline import analyze_timeline

class TestTimelineAnalyzer(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(analyze_timeline([]), {})

if __name__ == "__main__":
    unittest.main()
