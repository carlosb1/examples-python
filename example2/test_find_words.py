import unittest
from find_words import WordFinder
import os
import string




def load_dictionary(filename):
	import re
	dictionary={}
	with open(filename) as f:
		content = f.readlines()
	
	for word in content:
		word = re.sub('[^a-zA-Z0-9-_*.]','',word)
		if len(word) > 0:
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
	
        def test_load_dictionary(self):
		dic = load_dictionary("./dictionary.txt")
		self.assertEquals(dic["work"],"work")
                self.assertEquals(dic["man"],"man")
                self.assertEquals(dic["workman"],"workman")

	def test_generate_random_letters(self):
		values = generate_random_letters(10)
		self.assertTrue(len(values) > 0)
        
        def test_possible_words_simple_word(self):
                values = ['z','o','o']
                dictionary = load_dictionary("./dictionary.txt")
                finder = WordFinder(dictionary)
                correct_words = finder.create_possible_words(values)
		print correct_words
                #self.assertTrue(len(correct_words)==4)


        def test_possible_words(self):
                values = ['w','o','r','k','m','a','n']
                dictionary = load_dictionary("./dictionary.txt")
                finder = WordFinder(dictionary)
                correct_words = finder.create_possible_words(values)
		print correct_words
		#self.assertTrue(len(correct_words)==2)
        def test_one_letter_incorrect_character(self):
		dictionary = load_dictionary("./dictionary.txt") 
                letters = ['z']
                finder = WordFinder(dictionary)
                values = finder.find(letters)
		print values
		#self.assertTrue(values[0])

	def test_one_letter(self):
		dictionary = load_dictionary("./dictionary.txt") 
                letters = ['a']
                finder = WordFinder(dictionary)
                values = finder.find(letters)
		print values
		#self.assertTrue(values[0])

        def test_simple_word(self):
		dictionary = load_dictionary("./dictionary.txt") 
                letters = ['h','e','l','l','o']
                finder = WordFinder(dictionary)
                values = finder.find(letters)
		print values
        
	def test_simple_words(self):
		dictionary = load_dictionary("./dictionary.txt") 
                letters = ['h','e','l','l','o','w','o','r','l','d']
                finder = WordFinder(dictionary)
                values = finder.find(letters)
                print values

if __name__ == '__main__':
	unittest.main()

