# python 3.3
# Solution checker (this is rather a sanity checker than a full solution checker)
# For details see: http://goo.gl/ruHIYp

numberLines = list()

inputFilename = r'input.txt'

with open(inputFilename, 'r') as infile:
    for line in infile:
        numberLines.append( list(map(lambda s : int(s,2), line.strip().split())))

def checkSolution( numberLines ):
    len(numberLines)
    if len(numberLines) < 2 or len(numberLines[0]) != 2 or len(numberLines[-1]) != 1:
        return 1
    
    product = numberLines[0][0] * numberLines[0][1]
    for line in numberLines[1:]:
        if sum( line ) != product:
            print(line)
            return 2
    
    for line, nextline in zip( numberLines[1:-2], numberLines[2:-1] ):
        while len( line ) >= 3 and len( nextline ) >= 2:
            if sum( line[:3] ) != sum( nextline[:2] ):
                return 3
            line = line[3:]
            nextline = nextline[2:]
        if line != nextline:
            return 4
    
    return 0

result = checkSolution( numberLines )
if result == 0:
    print( 'Correct solution' )
else:
    print (result)
    print( 'Wrong solution' )