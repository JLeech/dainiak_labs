# -*- coding: utf-8 -*-
def checkSolution():
    codewords = set()
    with open( 'input.txt' ) as infile:
        codewords = set(infile.read().split())
    
    p = len(codewords) - 1
    
    if p < 3 or p % 4 != 3 or len( [1 for n in range(1, p) if p % n == 0 ]) > 1: 
        return( 'Unable to open file or file read error' )
    
    if set( map( len, codewords ) ) != set([p,]):
        return( 'Error: codewords have inappropriate sizes' )
    
    from itertools import combinations
    
    for w1, w2 in combinations( codewords, 2 ):
        if len([ 1 for (x,y) in zip( w1, w2 ) if x != y ]) < ( p + 1 ) // 2:
            return( 'Error: distance too small between words ' + w1 + ' and ' + w2 )
            
    return( 'All tests passed' )
    
if __name__ == "__main__":
    print( checkSolution() )