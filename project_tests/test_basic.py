import unittest
from calc import add

class TestBasic(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(2,2), 4)
	def test_add(self):
		self.assertEqual(add(4,4), 8)
