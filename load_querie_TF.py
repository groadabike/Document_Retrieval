'''
------------------------------------------------------------
Created on Nov 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Registration Number  = 150105918
------------------------------------------------------------
'''

from nested_dictionary import NestedDict
import math


class LoadQuerie_TF(object):
    '''
    This Class load the queries and process Term Weigth by Binary
    '''


    def __init__(self, querieIndex,index,collectionVector):
        '''
        Constructor
        '''
        self.__indexDict    = index
        #self.__querieFile   = querieFile
        self.__collectionVector = collectionVector
        
        self.__querieDict = querieIndex
        self.__querieVector = self.__querieLengthVector()
        self.__resultDict = self.__retrievalTF()    
         
         
    def __querieLengthVector(self):
        querieVector = NestedDict()
        for q in self.__querieDict:
            querieVector[q]=0
            vector = 0 
            for w in self.__querieDict[q]:
                vector += float(self.__querieDict[q][w])**2
            querieVector[q] = math.sqrt(vector)
        return querieVector        
    
    
    def __retrievalTF(self):
        resultDict = NestedDict()
        for q in self.__querieVector:
            for w in self.__querieDict[q]: 
                for d in self.__collectionVector:
                    if q not in resultDict:
                        resultDict[q][d] = 0
                    if d not in resultDict[q]:
                        resultDict[q][d] = 0
                    if d in self.__indexDict[w]:
                        resultDict[q][d] += self.__indexDict[w][d]*self.__querieDict[q][w]
                
        for q in self.__querieVector: 
            for d in self.__collectionVector:
                resultDict[q][d] = resultDict[q][d] / (self.__collectionVector[d]* self.__querieVector[q])
                
        return  resultDict  
    
    
    def getResultDict(self):
        return self.__resultDict

