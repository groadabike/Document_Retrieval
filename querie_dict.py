'''
------------------------------------------------------------
Created on Nov 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Registration Number  = 150105918
------------------------------------------------------------
'''
from read_documents import ReadDocuments
from tokenizator import Tokenizator
from stemmator import Stemmator
from nested_dictionary import NestedDict 

class QuerieDict(object):
    '''
    Class create querie Dict
    '''


    def __init__(self, qf,one,tok,stem, stop,strWords,optR):
        '''
        Constructor
        '''
        self.__stem = stem
        self.__stoplist = stop
        if optR:
            self.__querieDict = self.__CreateStringDictionary(strWords)
        else:
            self.__querieFile= qf
            self.__tok = tok
            self.__querieDict = self.__CreateQuerieDict(one)
    
    
    def __CreateQuerieDict(self,onequerie):
        print 'Loading Queries...'
        documents = ReadDocuments(self.__querieFile)
        queries = NestedDict()
        for doc in documents:
            docid = doc.docid
            if onequerie!= 0:
                if  docid != onequerie:
                    continue
    
            for line in doc.lines: 
                token = Tokenizator(line,self.__tok).toToken()
                
                for tok in token:
                    word = Stemmator(tok,self.__stem).toStem()
                        
                    if word not in self.__stoplist:
                        if word not in queries[docid]:
                            queries[docid][word]=0
                        queries[docid][word]+=1
                        
        print 'Queries loaded...'  
        return queries 
    
    def __CreateStringDictionary(self,strWords):
        print 'Loading Queries...'
        query = NestedDict()
        for s in strWords:
            s =  Stemmator(s,self.__stem).toStem()
            if s not in self.__stoplist:
                if s != '.':
                    
                    if s in query[0]:
                        query[0][s] += 1
                    else: 
                        query[0][s]=1
        print 'Queries loaded...'  
        return query
    
    def getQueryDict(self):
        return self.__querieDict