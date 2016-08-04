'''
------------------------------------------------------------
Created on Oct 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Registration Number  = 150105918
------------------------------------------------------------
'''

from command_line import CommandLine
from stop_list import StopList
from create_index import CreateIndex
from load_querie_TFIDF import LoadQuerie_TFIDF
from load_querie_TF import LoadQuerie_TF
from load_querie_B import LoadQuerie_B
from print_result import PrintResult
from querie_dict import QuerieDict

if __name__ == '__main__':
    commandLine = CommandLine()
    
    #################################
    #        Load StopList          #
    #################################
    stop = StopList(commandLine.getStopListFile(),commandLine.getStem())
    
    #################################
    #        Load IndexFile         #
    #################################
    if (commandLine.getCreateIndex()):
        index = CreateIndex(commandLine.getIndexFile(),stop.stops, commandLine.getCollection(),True,commandLine.getStem(), commandLine.getToken())
    else:
        index = CreateIndex(commandLine.getIndexFile())
    
    
    if(commandLine.getWeigthMethod()!= None):
        #################################
        #        Load Queries           #
        #################################
        if (commandLine.getStringQuery() == None):
            myQueryDict = QuerieDict(commandLine.getQuerieFile(),commandLine.getOneQuerie(),commandLine.getToken(),commandLine.getStem(),stop.stops, "",False )
        else:
            myQueryDict = QuerieDict(None,None,None,commandLine.getStem(),stop.stops,commandLine.getStringQuery() ,True )
        #################################
        #     Vector Weigth Binay       #
        #################################
        if (commandLine.getWeigthMethod() == 'B'):
            if (commandLine.getQuerieFile() != None):
                myLoadQuerie = LoadQuerie_B(myQueryDict.getQueryDict(),index.getIndex())
                querie = myLoadQuerie.getResultDict()
        
        #################################
        #       Vector Weigth TF        #
        #################################
        elif (commandLine.getWeigthMethod() == 'F'):
            if (commandLine.getQuerieFile() != None):
                myLoadQuerie = LoadQuerie_TF(myQueryDict.getQueryDict(),index.getIndex(),index.getDocumentVector())
                querie = myLoadQuerie.getResultDict()
        
        
        #################################
        #      Vector Weigth TF.IDF     #
        #################################
        elif (commandLine.getWeigthMethod() == 'D'):
            #if (commandLine.getQuerieFile() != None):
            myLoadQuerie = LoadQuerie_TFIDF(myQueryDict.getQueryDict(),index.getIDFDict() ,index.getDocumentVector(),index.getTFIDFDict() )
            querie = myLoadQuerie.getSimilarity()
            
        result = PrintResult(querie,commandLine.getResultAmount(),commandLine.getWeigthMethod(),commandLine.getResultFile() )    
  
        
        
        
        
        
        
        
        
        
        
        
        
        