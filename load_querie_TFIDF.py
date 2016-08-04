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

class LoadQuerie_TFIDF():
    '''
    This Class load the queries and process Term Weigth by TF.IDF
    '''


    def __init__(self,querieIndex, idf_Collection,documentVector,tfidfCollection):
        '''
        Constructor
        '''
        self.__idf_Collection = idf_Collection      #Collection IDF
        self.__tf_idf_Querie = NestedDict()         #Dictionary of Queries TF.IDF
        self.__querieVector = NestedDict()          #Dictionary with Queries Length Vector
        self.__documentVector = documentVector      #Dictionary with Document Length Vector
        self.__TFIDFCollection = tfidfCollection    #Dictionary of TFIDF Collection
        
        self.__querieDict = querieIndex             #Load Querie Dictionary
        self.__getQuerieTFIDF()                     #Load Querie TFIDF Dictionary
        self.__querieLengthVector()                 #Calculate the Querie Length Vector and fill __querieVector
        self.__resultDict = NestedDict()            #Dictionary of result
                
        
    def __getQuerieTFIDF(self):
        for q in self.__querieDict:
            for w in self.__querieDict[q]:         
                self.__tf_idf_Querie[q][w.encode('ascii')]=0
                if w in self.__idf_Collection:
                    self.__tf_idf_Querie[q][w.encode('ascii')] += self.__idf_Collection[w]*self.__querieDict[q][w]


    def __querieLengthVector(self):
        for q in self.__tf_idf_Querie:
            self.__querieVector[q]=0
            vector = 0 
            for w in self.__tf_idf_Querie[q]:
                vector += float(self.__tf_idf_Querie[q][w])**2
            self.__querieVector[q] = math.sqrt(vector)
            
    
    def getSimilarity(self):
        for q in self.__querieVector:
            for d in self.__documentVector:
                self.__resultDict[q][d] = 0
                for w in self.__tf_idf_Querie[q]:
                    if w in self.__TFIDFCollection[d]:
                        self.__resultDict[q][d] += self.__TFIDFCollection[d][w]*self.__tf_idf_Querie[q][w]
                
                self.__resultDict[q][d] = self.__resultDict[q][d] / (self.__documentVector[d]* self.__querieVector[q])
        return   self.__resultDict  

    
    
    def __getitem__(self,item):
        return self.__tf_idf_Querie[item]

       
if __name__ == '__main__':
    querie =  LoadQuerie_TFIDF( '../files/queries.txt',set(),{'perro':2.22530928173,'gato':3.50569250741,'pez':3.50569250741})
    print querie['perro']