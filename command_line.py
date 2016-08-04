# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
Created on Oct 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Registration Number  = 150105918
------------------------------------------------------------
USE: 
    python <PROGNAME> (options) 
    
OPTIONS:
Help :
    -h : print this help message and exit

PARAMETERS/BEHAVIOURS:
    -c FILE : FILE as a COLLECTION_FILE. 
    -q FILE : FILE as a QUERIE_FILE
    -p INT : INT is the id of one query inside the QUERIE_FILE. This is a filter of "-q" option, and works together.
    -t STRING : STRING is a string of query words separated each by full stop ".". This option cannot be together with "-q" option. 
    -i FILE : FILE as a name of INDEX_FILE. If it is not specify one, the system will assume "index.txt" by default. This option only work with "-c" option declared.
    -I : the file INDEX_FILE must be created before use it.
    -r FILE : FILE as a RESULT_FILE. If not present but option "B" or "-F" or "-D" are declared, result is printed in screen. 
    -a INT : INT as a length of output ranking. By default the value is 10.
    -s FILE : FILE as a STOPLIST_FILE
    -S : use PorterStemmer. 
    -L : use LancasterStemmer.
If none options, "-S" or "-L", are declared, system will not use stemmed process.
If both options, "-S" and "-L", are declared, system use PorterStemmer.
    -T : apply TreebankWordTokenizer. The system work with WordPunctTokenizer by default. 
    -B : term weight in vector are BINARY.
    -F : term weight in vector are TERM FREQUENCY.
    -D : term weight in vector are TF.IDF.
Only one of the options "-B", "-F" and "-D" can be declared.
        
EXAMPLES:
    - Create default index of collection COLLECTIONFILE without stop list, using PorterStemmer and WordPunctTokenizer
    python <PROGNAME> -c COLLECTIONFILE -I -S
    
    - Create index INDEXFILE without stop list, using LancasterStemmer and WordPunctTokenizer
    python <PROGNAME> -c COLLECTIONFILE -i INDEXFILE -I -L
    
    - Retrieve Document using QUERIEFILE, a exist INDEXFILE, saving in OUTPUTFILE using STOPLISTFILE, PorterStemmer, TreebankWordTokenizer and Term Frequency Aproach
    python <PROGNAME> -q QUERIEFILE -i INDEXFILE -r OUTPUTFILE -s STOPLISTFILE -S -T -F
------------------------------------------------------------
'''


import sys, getopt
from tokenizator import Tokenizator


class CommandLine:
    def __init__(self):   
        opts, args = getopt.getopt(sys.argv[1:],'hc:q:p:t:i:Ir:a:s:SLTBFD')
        opts = dict(opts)
        
        self.__stoplistFile = None
        self.__indexFile = 'index.txt'
        self.__porterStemmer = False
        self.__lancasterStemmer = False
        self.__collection = None
        self.__wpToken = True
        self.__twToken = False
        self.__createIndex = False
        self.__querieFile = None
        self.__weigthMethod = None
        self.__resultFile = None
        self.__resultAmount = 10
        
        self.__oneQuerie = 0
        self.__stringQuerie = None
        
        if '-h' in opts:
            self.__printHelp()
        
        if '-q' in opts and '-t' in opts:
            print >> sys.stderr, "\n** ERROR: Cannot select query FILE and query STRING at the same time **"
            self.__printHelp() 

        if '-c' not in opts and '-I' in opts:
            print >> sys.stderr, "\n** ERROR: Must specify a collection file name (opt: -c) in order to create index (opt: -I) **"
            self.__printHelp() 
        
        if self.__getAmountWeigth(opts)>1:
            print >> sys.stderr, "\n** ERROR: Cannot specify more than one Vector Weigth Method **" 
            self.__printHelp() 

        if '-c' in opts:
            self.__collection = opts['-c']
        
        if '-q' in opts:
            self.__querieFile = opts['-q']
        
        if '-p' in opts:
            self.__oneQuerie = int(opts['-p'])
    
        
        if '-i' in opts:
            self.__indexFile = opts['-i']
            
            
        if '-I' in opts:
            self.__createIndex = True
        
        if '-r' in opts:
            self.__resultFile = opts['-r']
        
        if '-a' in opts:
            self.__resultAmount = int(opts['-a'])
            
        if '-s' in opts:
            self.__stoplistFile = opts['-s'] 
        
        if '-L' in opts:
            self.__porterStemmer = False
            self.__lancasterStemmer = True
        
        if '-S' in opts:
            self.__porterStemmer = True
            self.__lancasterStemmer = False
            
        if '-T' in opts:
            self.__wpToken = False
            self.__twToken = True
          
        if '-t' in opts:
            self.__stringQuerie = self.__loadStringQuery(opts['-t'])
                
        if '-B' in opts:
            self.__weigthMethod = 'B'
        elif '-F' in opts:
            self.__weigthMethod = 'F'
        elif '-D' in opts:
            self.__weigthMethod = 'D'
           
    def __printHelp(self):
        help = __doc__.replace('<PROGNAME>',sys.argv[0],1)
        print '\n','-' * 60 , '\n' , sys.stderr, help, '\n'
        exit()
              
    def __getAmountWeigth(self, opts):
        amount = 0
        if '-B' in opts:
            amount += 1
        if '-D' in opts:
            amount += 1
        if '-F' in opts:
            amount += 1 
        return amount
    
    def getCollection(self):
        return self.__collection
    
    def getStopListFile(self):
        return self.__stoplistFile
    
    def getIndexFile(self):
        return self.__indexFile
    
    def getQuerieFile(self):
        return self.__querieFile
    
    def getCreateIndex(self):
        return self.__createIndex
    
    def __getWPToken(self):
        return self.__wpToken
    
    def __getTWToken(self):
        return self.__twToken
    
    def __getPorterStemmer(self):
        return self.__porterStemmer
    
    def __getLancasterStemmer(self):
        return self.__lancasterStemmer
    
    def getStem(self):
        if self.__getLancasterStemmer():
            return 'Lancaster'
        elif self.__getPorterStemmer():
            return 'Porter'
        else:
            return 'None'
        
    def getToken(self):
        if self.__getWPToken():
            return 'WPT'
        elif self.__getTWToken():
            return 'TWT'
        
    def getWeigthMethod(self):
        return self.__weigthMethod
    
    def getResultAmount(self):
        return self.__resultAmount
    
    def getResultFile(self):
        return self.__resultFile
    
    def getOneQuerie(self):
        return self.__oneQuerie
        
    def __loadStringQuery(self,opts):
        t = Tokenizator(opts,'WPT').toToken()
        return t
    
    def getStringQuery(self):
        return self.__stringQuerie
    
    
if __name__=='__main__':
    command = CommandLine()
    print "Collection : " , command.getCollection()
    print "Stop List file : " , command.getStopListFile()
    print "Index File : " , command.getIndexFile()
    print "Querie File : " , command.getQuerieFile()
    print "Create Index File : " , command.getCreateIndex()
    print "Use Tokenization : " , command.getToken()
    print "Use Stemmer : " , command.getStem()
    print "Weigth Method : " , command.getWeigthMethod()
    print "Query : ", command.getStringQuery() 

