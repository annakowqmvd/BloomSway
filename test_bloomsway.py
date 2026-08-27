# test_bloomsway.py
"""
Tests for BloomSway module.
"""

import unittest
from bloomsway import BloomSway

class TestBloomSway(unittest.TestCase):
    """Test cases for BloomSway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BloomSway()
        self.assertIsInstance(instance, BloomSway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BloomSway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
