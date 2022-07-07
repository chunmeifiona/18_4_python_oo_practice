"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    '''Machine for finding random words from dictionary
    >>> wf = WordFinder("animal.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    
    '''
    def __init__(self, path):
        self.path = path

        wordfile = open(self.path,"r")

        self.word_list = self.funList(wordfile)

        print(f"{len(self.word_list)} words read")
        wordfile.close()
    
    def random(self):
        return choice(self.word_list)

    def funList(self, wordfile):
        return [line[:-1] if line[-1]=='\n' else line for line in wordfile]
    

class SpecialWordFinder(WordFinder):
    '''Specialized WordFinder that excludes blank lines/comments
    >>> swf = SpecialWordFinder("special.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    '''
    def funList(self, wordfile):
        wordlist = []
        for line in wordfile:
            if line[0] != '#' and line.isspace() == False:
                if line[-1] == '\n':
                    wordlist.append(line[:-1])
                else:
                    wordlist.append(line)
        return wordlist
            

    

    
        