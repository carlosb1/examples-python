#!/usr/bin/python
import sys

class Cell(object):
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def __str__(self):
        return "("+str(self.row)+","+str(self.col)+")"

class SolvedCell(object):
    def __init__(self,row,col,value):
        self.value=value
        self.row = row
        self.col = col
    def __str__(self):
        return "("+str(self.row)+","+str(self.col)+") value="+str(self.value)
    
class Rule(object):
    def __init__(self,value,cells):
        self.cells = cells
        self.value = value    
    def __str__(self):
        retStr = "value="+str(self.value)+ " cells=[ "
        for cell in self.cells:
            retStr+=str(cell)+" "
        retStr+="]"
        return retStr

FRSTVALUE = ord('A')

#Get content from file 
siz = len(sys.argv)
if siz < 2:
    print "usage: kakuro.py input.txt"
    sys.exit()

content = [line.rstrip('\n') for line in open(str(sys.argv[1]),'r')]


#Process first line of file
firstline = content[0]
sizes = firstline.split(' ')
if len(sizes) <2:
    print "Size configuration parameters are wrong"

size_cols=int(sizes[0])
size_rows=int(sizes[1])

cols = [ chr(c) for c in xrange(FRSTVALUE,FRSTVALUE+size_cols) ]
rows = [ str(r) for r in xrange(1,1+size_rows) ]


#Process second line of file
sum_params = content[1:]
sums = str(sum_params).split(' ')
if len(sums) < 2:
    print "Configuration cells  are wrong"

#Set up matr with values
#matr=[x[:] for x in [[0]*size_rows]*size_cols]
rules = []
#rows x cols
for params in sum_params:
    params = params.split(' ')
    value = int(params[0])
    cells = []
    for posic in params[1:]:
        col = ord(str(posic)[0])-FRSTVALUE
        row = int(str(posic)[1]) -1
        cell = Cell(row,col)
        cells.append(cell)
    rules.append(Rule(value,cells))



for rule in rules:
    print rule


board=[x[:] for x in [[0]*size_rows]*size_cols]

solvedCells=[]
for rule in rules:

    solvedCells.append(solvedCell)


print cols
print rows
print content

