import unittest
from find_words import find_words
import os
import string




def load_dictionary(filename):
	import re
	dictionary={}
	with open(filename) as f:
		content = f.readlines()
	
	for word in content:
		word = re.sub('[^a-zA-Z0-9-_*.]','',word)	
		dictionary[word]=word

	return dictionary

def generate_random_letters(siz_letters):
	import string
	import random
	values = [random.choice(string.lowercase) for x in range(0,siz_letters)]
	return values


    #Acceptance tests
    #Unit tests
    #Functional tests
class TestFindWords(unittest.TestCase):
	def test_load_dictionary(self):
		dic = load_dictionary("./dictionary.txt")
		self.assertTrue(len(dic) > 0)
	def test_generate_random_letters(self):
		values = generate_random_letters(10)
		print values
		self.assertTrue(len(values) > 0)

	def test_normal_case(self):
		dictionary = load_dictionary("./dictionary.txt")
		values = generate_random_letters(30)
		phrase = find_words(dictionary,)


		pass

if __name__ == '__main__':
	unittest.main()

