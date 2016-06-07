import unittest
from calculate import Calculate

class TestCalculate(unittest.TestCase):
	def setUp(self):
		self.calc = Calculate()
		
	def test_add_ret_correctly(self):
		self.assertEqual(4, self.calc.add(2,2),"No add correctly, FAIL")
		
	def test_add_strings_raise_error(self):
		self.assertRaises(TypeError, self.calc.add, 'hello', 'world') 
		
	def test_add_ret_float_correctly(self):
		self.assertEqual(6.81, self.calc.add(4.51,2.3),"No add floats correctly, FAIL")
		
	def test_sub_ret_correctly(self):
		self.assertEqual(3, self.calc.sub(9,6),"No subtract correctly, FAIL")
		
	def test_mult_ret_correctly(self):
		self.assertEqual(6, self.calc.mult(2,3),"No multiply correctly, FAIL")
	
	def test_div_ret_correctly(self):
		self.assertEqual(3, self.calc.div(9,3),"No divide correctly, FAIL")
		
if __name__ == '__main__':
	unittest.main()
