#!/usr/bin/env python

import numpy as np
board=np.zeros((8,8),dtype='int64')
board[:3]=1
board[-3:]=2
#print(board)
#print(type(board))
a,b,c,d,e,f,g,h=0,1,2,3,4,5,6,7
class Board(object):
    def __init__(self):
        self._=np.zeros((8,8),dtype='int64')
        self._[:3]=1
        self._[-3:]=2
    def move(self,fro=(2,1),to=(3,0)):
        if self.validated(fro,to):
            self._[to[0]][to[1]]=self._[fro[0]][fro[1]]
            self._[fro[0]][fro[1]]=0
            print(self._)
    def validated(self,fro,to):
        return True
    def __str__(self):
        return str(self._)
demo=Board()
print("A B C D E F G H")
print(demo)
print("A B C D E F G H")
print("A B C D E F G H")
demo.move()
print("A B C D E F G H")
