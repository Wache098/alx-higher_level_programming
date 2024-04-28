# tests/test_models/test_base.py

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_incrementation(self):
        """Test that ids are incremented correctly."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test that a custom id is assigned correctly."""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_negative_custom_id(self):
        """Test that passing a negative id raises ValueError."""
        with self.assertRaises(ValueError):
            b = Base(-1)

if __name__ == '__main__':
    unittest.main()
