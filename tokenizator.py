'''
------------------------------------------------------------
Created on Oct 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Regitration Number  = 150105918
------------------------------------------------------------
'''

from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
import re

class Tokenizator():
    '''
    classdocs
    '''


    def __init__(self,t,style):
        '''
        Constructor
        '''
        self.__token = t
        self.__style = style
    
    
    def toToken(self):
        if self.__style == 'WPT':
            return WordPunctTokenizer().tokenize(self.__token)
        elif self.__style == 'TWT':
            return TreebankWordTokenizer().tokenize(self.__token)


if __name__=='__main__':
    token = Tokenizator("In Dusseldorf I took my hat off. But I can't put it back on.",'WPT')
    print token.toToken()
    token = Tokenizator("In Dusseldorf I took my hat off. But I can't put it back on.",'TWT')
    print token.toToken()
        