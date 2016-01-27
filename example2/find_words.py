
class WordFinder(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    """
    Function to find words
    """
    def find(list_of_letters):
        #TODO check words   
        if list_of_letters == None:
            return []
        set_of_find_words = []
        recur_find(list_of_letters,set_of_find_words) 
        return set_of_find_words

        
    def recur_find(list_of_words,set_of_find_words):
        if len(list_of_words) == 0 :
            return True
        for index_letters in range(1,len(list_of_words)):
            letters = list_of_words[0:index_letters]
            possible_words= create_possible_words(letters)
            if len(possible_words):
                return False
            #Append por insert
            for word in possible_words:
                set_of_find_words.append(word)
                #Check index
                result = recur_find(list_of_words[index_letters:],set_of_find_words)
                #It is a correct word, it is not necessary continue searching
                if result: 
                    return True
            


        #letters_to_setup = list_of_words[0]
        #possible words
        #possible_words = [ for ] 

        return True   

