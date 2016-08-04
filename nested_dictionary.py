'''
------------------------------------------------------------
Created on Oct 2015 by
    Name                = Gerardo Roa Dabike
    University ID       = acp15gr
    Regitration Number  = 150105918
------------------------------------------------------------
'''

class NestedDict(dict):
    
    def __missing__(self, key):
        self[key] = NestedDict()
        return self[key]
        

 
        
if __name__ == '__main__':
    table = NestedDict()
    table['A']['B1']['C1'] = 1
    table['A']['B1']['C1'] += 1
    if 'A' in table:
        print table['A']
        if 'B1' in table['A']:
            print table['A']['B1']
        print table