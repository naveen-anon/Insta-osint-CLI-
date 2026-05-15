# tests/test_collectors.py
import unittest
from collectors.profile import collect_profile

class TestProfileCollector(unittest.TestCase):
    def test_profile_fetch(self):
        data = collect_profile("natgeo")  # public account
        self.assertIn("username", data)
        self.assertEqual(data["username"], "natgeo")

if __name__ == "__main__":
    unittest.main()
