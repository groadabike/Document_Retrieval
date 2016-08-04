'''
------------------------------------------------------------
Created on Nov 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Registration Number  = 150105918
------------------------------------------------------------
'''

from nested_dictionary import NestedDict

class LoadQuerie_B(object):
    '''
    This Class load the queries and process Term Weigth by Binary
    '''


    def __init__(self, querieDict,index):
        '''
        Constructor
        '''
        self.__indexDict    = index
        #self.__querieFile   = querieFile
        
        self.__querieDict = querieDict
        self.__resultDict = self.__retrievalBinary()    
           


    def __retrievalBinary(self):
        resultDict = NestedDict()
        for querie in self.__querieDict: 
            for word in self.__querieDict[querie]:
                if word in self.__indexDict:
                    for doc in self.__indexDict[word]:
                        if querie in resultDict:
                            if doc in resultDict[querie]:
                                resultDict[querie][doc] += 1
                            else:
                                resultDict[querie][doc]=1
                        else:
                            resultDict[querie][doc]=1
                            
        return resultDict
    
    def getResultDict(self):
        return self.__resultDict
        
    #def __createQuerieDict(self):
    #    print 'Loading Queries...'
    #    documents = ReadDocuments(self.__querieFile)
    #    queries = NestedDict()
    #    for doc in documents:
    #        docid = doc.docid

    #        for line in doc.lines: 
    #            token = Tokenizator(line,self.__tok).toToken()
                
    #            for tok in token:
    #                word = Stemmator(tok,self.__stem).toStem()
                        
    #                if word not in self.__stoplist and word not in string.punctuation:
    #                    if word not in queries[docid]:
    #                        queries[docid][word]=0
    #                    queries[docid][word]+=1
                        
    #    print 'Queries loaded...'  
    #    return queries 

