# test_cryptoc.py
"""
Tests for CryptoC module.
"""

import unittest
from cryptoc import CryptoC

class TestCryptoC(unittest.TestCase):
    """Test cases for CryptoC class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoC()
        self.assertIsInstance(instance, CryptoC)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoC()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
