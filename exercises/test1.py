
def check_parenthesis(input_str):
	sze = len(input_str)
	if (sze == 0):
		return [True,-1]
	stack = []
	
	index = 0
	while index < sze:
		value = input_str[index]
		if value == '(':
			stack.append(value)
		elif value == ')':
			if len(stack)==0:
				return [False,index]
			else:
				stack.pop()
		else:
			print 'Incorrect characters'
			return [False,index]

		index+=1

	if len(stack) == 0:
		return [True,-1]
	else:
		return [False,stack[0]]
	


import unittest
class TestPairParenthesis(unittest.TestCase):
	def test_first_example(self):
		self.assertTrue(check_parenthesis("")[0])

	def test_simple_correct_case(self):
		self.assertTrue(check_parenthesis("()")[0])

	def test_simple_incorrect_case(self):
		value=check_parenthesis(")(")
		self.assertFalse(value[0])
		self.assertTrue(value[1]==0)
	
	def test_complex_case(self):
		value=check_parenthesis("((())())()")
		self.assertTrue(value[0])

	def test_incorrect_value_case(self):
		value=check_parenthesis("(((#))())()")
		self.assertFalse(value[0])
		self.assertTrue(value[1]==3)

if __name__ == '__main__':
	unittest.main()

