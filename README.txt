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
