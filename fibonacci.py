#!/data/data/com.termux/files/usr/bin/env python
import argparse

def fibseq(n):
    seq=[0,1]
    for i in range(n-1):
        seq.append(seq[-1]+seq[-2])
    return seq
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-n', action='store', dest='nth')
    parsed=parser.parse_args()
    n=parsed.nth
    print(fibseq(int(n)))

