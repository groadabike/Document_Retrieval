'''
------------------------------------------------------------
Created on Oct 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Regitration Number  = 150105918
------------------------------------------------------------
'''

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

class Stemmator():
    '''
    --------------------------------------
    - Stemmator Class apply the selected -
    - stemmer method to a word           -
    --------------------------------------
    '''
    
    def __init__(self,wr,style):
        '''
        -----------------------------
        - The object properties are -
        - a word and a stemmer      -      
        - style                     -
        -----------------------------
        '''
        self.__wordToStemmer = wr
        self.__style = style

  
    
    def toStem(self): 
        '''
        ----------------------------------------
        -  toStem methos apply the selected    -
        -  stemmer style and return the result -
        -  in lowercase                        -
        ----------------------------------------
        '''
        if self.__style=='Porter':
            #Apply Porter Stemmer
            stemm = PorterStemmer()
            return stemm.stem(self.__wordToStemmer).lower()
        
        elif self.__style == 'Lancaster':
            #Apply Lancaster Stemmer
            stemm = LancasterStemmer() 
            return stemm.stem(self.__wordToStemmer).lower()  
        
        elif   self.__style == 'None':
            #Just return the lower case of the word
            return self.__wordToStemmer.lower()             
        
 

if __name__=='__main__':
    word = "CODING"
    ste = Stemmator(word,'Porter').toStem()
    ste2 = Stemmator(word,'Lancaster').toStem()
    ste3 = Stemmator(word,'None').toStem()
    
    print word , ' Porter     -> ' ,ste
    print word , ' Lancaster  -> ' ,ste2
    print word , ' None       -> ' ,ste3