# tests/test_models/test_rectangle.py

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_constructor_with_no_id(self):
        """Test constructor with no custom id."""
        r = Rectangle(10, 20, 5, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_constructor_with_id(self):
        """Test constructor with custom id."""
        r = Rectangle(10, 20, 5, 5, 100)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_width(self):
        """Test width property."""
        r = Rectangle(10, 20, 5, 5)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_height(self):
        """Test height property."""
        r = Rectangle(10, 20, 5, 5)
        r.height = 40
        self.assertEqual(r.height, 40)

    def test_x(self):
        """Test x property."""
        r = Rectangle(10, 20, 5, 5)
        r.x = 15
        self.assertEqual(r.x, 15)

    def test_y(self):
        """Test y property."""
        r = Rectangle(10, 20, 5, 5)
        r.y = 25
        self.assertEqual(r.y, 25)

if __name__ == '__main__':
    unittest.main()
