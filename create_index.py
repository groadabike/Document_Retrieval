"""
------------------------------------------------------------
Created on Oct 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Registration Number  = 150105918
------------------------------------------------------------
"""

from stemmator import Stemmator
from tokenizator import Tokenizator
from read_documents import ReadDocuments
from nested_dictionary import NestedDict
import re, math

class CreateIndex():
    '''
    ----------------------------------------------
    - This Class create/load the index INDEXFILE -
    ----------------------------------------------
    '''


    def __init__(self, iF ,sl=None,c=None,create=False,stem=None,tok=None):
        '''
        -------------------------------------------------
        -    iF       : Index File
        -    sl       : Stoplist Set
        -    c        : Collection File
        -    create   : Boolean that indicate if the index should be created first or not
        -    stem     : Stemmer method
        -    tok      : Tokenization method
        -------------------------------------------------
        '''
        if sl==None:
            self.__stoplist = set()
        else:
            self.__stoplist = sl        #StopList(sl).stops #sl
        
        self.__stem = stem              #Stemmer method
        self.__tok = tok                #Token method
        self.__indexFile = iF           #Index File
        self.__collection = c           #Collection File
        self.__collectionSize = 0       #Total Number Documents in Collection
        self.__index = NestedDict()     #Index Dictionary
        self.__dic_df = NestedDict()    #Document frequency Dictionary
        self.__dic_idf = NestedDict()   #Inverse Document frequency Dictionary
        self.__dic_tfidf = NestedDict() #tf*idf dictionary
        self.__dictVector = NestedDict()#Length of the vector
        
        if create:
            #Create Index file and return the dictionary
            self.createIndexFile()
            
        else:
            #Load Index files and return the dictionary
            self.loadIndexFile()
    
    def createIndexFile(self):
        print 'Starting Index Creation...'
        #Open Collection File
        documents = ReadDocuments(self.__collection)
        for doc in documents:
            #Load Document Id
            docid = doc.docid
            #Counting collection Size
            self.__collectionSize += 1
            
            for line in doc.lines: 
                token = Tokenizator(line,self.__tok).toToken()
                
                for tok in token:
                    word = Stemmator(tok,self.__stem).toStem()
                    
                    if word not in self.__stoplist:
                        if word not in self.__index:
                            self.__index[word][docid]=1
                            self.__dic_df[word] = 1
                            
                        else:
                            if docid in self.__index[word]: 
                                self.__index[word][docid] += 1
                                
                            else: 
                                self.__index[word][docid] = 1
                                self.__dic_df[word] += 1

        f = open(self.__indexFile , 'w')                    
        print >>f ,"<IndexFile Size_Collection=" , int(self.__collectionSize) ,">\n"
        for word in self.__index:
            self.__dic_idf[word] = math.log10(self.__collectionSize/self.__dic_df[word])
            print >>f ,"\t<word=" , word ," document_frequency=" ,self.__dic_df[word], " inverse_document_frequency=" , self.__dic_idf[word] , ">" 
            for idoc in self.__index[word]:
                self.__dic_tfidf[idoc][word] = int(self.__index[word][idoc]) * self.__dic_idf[word]
                print >>f ,"\t\t<iddoc=" , int(idoc) ," term_frequency=" ,int(self.__index[word][idoc]) ," tfidf=" ,self.__dic_tfidf[idoc][word], " />"
            print >>f , "\t</word>\n"
        print >>f ,"</IndexFile>"
        f.close()
        print 'Index Created...'                        
        return self.__index
    
    def __getitem__(self, index):
        return self.__index[index]      
         
    def loadIndexFile(self):
        firstlineword = re.compile('\s*<IndexFile Size_Collection=\s*(\d+)\s*>')
        startword = re.compile('\s*<word=\s*(.+) \s* document_frequency=\s*(\d+)\s* inverse_document_frequency=\s*(\d+.\d+)\s* >')
        endword = re.compile('\s*</word>')
        source = re.compile('\s*<iddoc=\s*(\d+)\s* term_frequency=\s*(\d+)\s* tfidf=\s*(\d+.\d+)\s* />')
        readingWord = False
        print 'Loading Index...'
        firstline = True
        with open(self.__indexFile) as input_fs:
            for line in input_fs:
                if firstline == True:
                    #Reading Collection Size
                    m = firstlineword.search(line)
                    word = m.group(1)
                    self.__collectionSize = word
                    firstline = False
                
                else:
                    m = startword.search(line)
                    if m:
                        #Reading Word
                        readingWord = True
                        word = m.group(1)
                        self.__dic_df[word] =  int(m.group(2))   
                        self.__dic_idf[word] = float(m.group(3))  
                     
                    elif endword.search(line):
                        readingWord = False
                        
                    elif readingWord:   
                        #Reading Documents where the word appear
                        w = source.search(line)
                        iddoc =  int(w.group(1)) 
                        count =  int(w.group(2))     
                        self.__index[word][iddoc]=count   
                        self.__dic_tfidf[iddoc][word] = float(w.group(3))
        print 'Index Loaded...'
        return self.__index   

    def getIDFDict(self):
        return self.__dic_idf
    
    def getTFIDFDict(self):
        return self.__dic_tfidf

    def getIndex(self):
        return self.__index
    
    def __documentLenghtVector(self):
        for d in self.__dic_tfidf:
            self.__dictVector[d]=0
            vector = 0
            for w in self.__dic_tfidf[d]:
                self.__dic_tfidf[d][w]
                vector += float(self.__dic_tfidf[d][w])**2
            self.__dictVector[d] = math.sqrt(vector)
    
    def getDocumentVector(self):
        self.__documentLenghtVector()
        return self.__dictVector
                    
if __name__=='__main__':
    index = CreateIndex(iF= '../files/index2.txt',sl='../files/stop_list.txt' ,c='../files/documents.txt',create=True,stem='Porter',tok='WPT')

                    
                    
                    
                    
                    
                    
        