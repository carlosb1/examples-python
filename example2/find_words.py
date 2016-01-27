
class WordFinder(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    """
    Function to find words
    """
    def find(self,list_of_letters):
        #TODO check words   
        if list_of_letters == None :
            return []
        set_of_find_words = []
        result = recur_find(list_of_letters,set_of_find_words) 
        return result[1]

        
    def create_possible_words(self,list_of_letters):
	import itertools
	all_possible_words = itertools.permutations(list_of_letters)
	correct_words = [''.join(possible_word) for possible_word in all_possible_words if self.dictionary.has_key(''.join(possible_word))]
	new_list = []
	[new_list.append(possible_word) for possible_word in correct_words if possible_word not in new_list]
	return new_list

    def recur_find(self,list_of_words,set_of_find_words):
        if len(list_of_words) == 0 :
            return [True,list_of_words]
        for index_letters in range(1,len(list_of_words)):
            letters = list_of_words[0:index_letters]
            possible_words= create_possible_words(letters)
            if len(possible_words):
                return [False,list_of_words]
            #Append por insert
            for word in possible_words:
                set_of_find_words.append(word)
                #Check index
                result = recur_find(list_of_words[index_letters:],set_of_find_words)
                #It is a correct word, it is not necessary continue searching
                if result[0]: 
                    return [True,list_of_words]


        return [False, list_of_words]

