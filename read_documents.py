"""
------------------------------------------------------------
FILE: read_documents
CLASS:ReadDocuments
------------------------------------------------------------
"""

import re, sys

class ReadDocuments:
    def __init__(self,file):
        self.collection_file = file

    def __iter__(self):
        startdoc = re.compile('<document docid\s*=\s*(\d+)\s*>')
        enddoc = re.compile('</document\s*>')
        readingDoc = False
        with open(self.collection_file) as input_fs:
            for line in input_fs:
                m = startdoc.search(line)
                if m:
                    readingDoc = True
                    doc = Document()
                    doc.docid = int(m.group(1))
                elif enddoc.search(line):
                    readingDoc = False
                    yield doc
                elif readingDoc:
                    doc.lines.append(line)

class Document:
    def __init__(self):
        self.docid = 0
        self.lines = []

    def printDoc(self,out = sys.stdout):
        print >> out, "\n[DOCID: %d]" % self.docid
        for line in self.lines:
            print >> out, line,

if __name__ == '__main__':
    documents = ReadDocuments("../files/queries.txt")
    for doc in documents:
        print "ID : ", doc.docid
        for l in doc.lines:
            print l
