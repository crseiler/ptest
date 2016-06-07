import numbers

class Calculate:
	def is_number(self, x):
		return isinstance(x, numbers.Number)
        
	def add(self, x, y):
		if self.is_number(x) and self.is_number(y):
			return x + y
		else:
			raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))
			
	def sub(self, x, y):
		if self.is_number(x) and self.is_number(y):
			return x - y
		else:
			raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))
			
	def mult(self, x, y):
		if self.is_number(x) and self.is_number(y):
			return x * y
		else:
			raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))
		
	def div(self, x, y):
		result = 0
		try:
			if self.is_number(x) and self.is_number(y):
				result =  x / y
		
		except ZeroDivisionError:
			raise ZeroDivisionError
			
		except TypeError:
			raise TypeError
			
		else:
			return result

if __name__ == '__main__':
	calc = Calculate()
	result = calc.add(2,2)
	print(result)
