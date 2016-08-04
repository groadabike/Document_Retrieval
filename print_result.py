'''
------------------------------------------------------------
Created on Nov 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Registration Number  = 150105918
------------------------------------------------------------
'''

class PrintResult(object):
    '''
    This Class recieve the relevants documents and print results
    '''


    def __init__(self, querieResult,countResults,method,exitFile):
        '''
        Constructor
        '''
        self.__querieResult  = querieResult
        self.__countResults  = countResults
        self.__method        = method
        self.__exitFile      = exitFile
        
        self.__printRelevantDocs()
        
        
    def __printRelevantDocs(self):
        print 'Creating output file...'
        if self.__exitFile != None:
            f = open(self.__exitFile  , 'w')
          
        for querie in self.__querieResult:
            docs = self.__querieResult[querie].keys()
            docs.sort(reverse=True, key = lambda d:self.__querieResult[querie][d])
            a = 0
            for doc in docs:
                if a < self.__countResults:
                    if querie < 10:
                        num = '0' + str(querie)
                    else:
                        num = str(querie)
                    
                    if doc < 10:
                        d = '000' + str(doc)
                    elif doc < 100:
                        d = '00' + str(doc)
                    elif  doc < 1000:
                        d = '0' + str(doc) 
                    else: 
                        d = str(doc)
                    if self.__exitFile != None:
                        print >>f, num ,d
                    else:
                        print num ,d
                    a += 1                    
                    
        if self.__exitFile != None:        
            if self.__method == 'B':
                print 'Output Binary file' , self.__exitFile , 'created...'
            elif self.__method == 'F':
                print 'Output Term Frequency file' , self.__exitFile , 'created...'
            elif self.__method == 'D':
                print 'Output TF.IDF file' , self.__exitFile , 'created...'
            f.close()
        else:
            if self.__method == 'B':
                print 'Output Binary...'
            elif self.__method == 'F':
                print 'Output Term Frequency...'
            elif self.__method == 'D':
                print 'Output TF.IDF...'