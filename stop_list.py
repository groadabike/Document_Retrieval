'''
------------------------------------------------------------
Created on Oct 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Regitration Number  = 150105918
------------------------------------------------------------
'''

from stemmator import Stemmator
import string

class StopList():
    '''
    This class load a stoplist file and return a SET with the list
    '''


    def __init__(self, file,stem):
        '''
        Constructor
        '''
        self.__stem = stem
        self.stops=set()
        self.__addStringPuntuation()
        if file != None:
            self.__readStopList(file)
    
    def __addStringPuntuation(self):
        for s in string.punctuation:
            self.stops.add(s)
            
        
    def __readStopList(self,file):
        '''
        Method that load the stoplist into 
        the stop SET 
        '''
        print 'Loading StopList...'
        f = open(file,'r')
        for line in f:
            self.stops.add(line.strip())
            #self.stops.add(Stemmator(line.strip(),self.__stem).toStem())
        print 'StopList Loaded...'


if __name__=='__main__':   
    stop = StopList('../files/stop_list.txt')
    for s in stop.stops:
        print s