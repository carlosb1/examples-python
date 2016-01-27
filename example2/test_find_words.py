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
		print dic["work"]
                print dic["man"]
                print dic["workman"]
	def test_generate_random_letters(self):
		values = generate_random_letters(10)
		self.assertTrue(len(values) > 0)
        
        def test_possible_words_simple_word(self):
                values = ['z','o','o']
                dictionary = load_dictionary("./dictionary.txt")
                finder = WordFinder(dictionary)
                correct_words = finder.create_possible_words(values)
                print correct_words


        def test_possible_words(self):
                values = ['w','o','r','k','m','a','n']
                dictionary = load_dictionary("./dictionary.txt")
                finder = WordFinder(dictionary)
                correct_words = finder.create_possible_words(values)
                print "test_possible_word",correct_words

        def test_first_case(self):
		dictionary = load_dictionary("./dictionary.txt")
                
                letters = ['a']
                finder = WordFinder(dictionary)
                #finder.find(letters)
		#print values

if __name__ == '__main__':
	unittest.main()

