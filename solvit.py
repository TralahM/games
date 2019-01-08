#!/data/data/com.termux/files/usr/bin/env python

import argparse
from random import sample

N=[i for i in range(1,10)]

if __name__=='__main__':
    ps=argparse.ArgumentParser()
    ps.add_argument('-s',action='store',dest='s')
    ps.add_argument('-n',action='store',dest='n')
    psd=ps.parse_args()
    s,n=int(psd.s),int(psd.n)
    if s>45:
        raise ValueError("S must not exceed 45")
    if n>9:
        raise ValueError("N must not exceed 9")
    res=sample(N,n)
    while sum(res)!=s:
        res=sample(N,n)
    print(sorted(res))

