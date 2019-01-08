#!/data/data/com.termux/files/usr/bin/env python
import argparse

def simple_interest(p,r,t):
    I=p*t*(r/100)
    A=p+I
    return A,I
def compound_interest(p,r,t):
    I=0.0
    A=p
    for i in range(t):
        I=A*(r/100)
        A+=I
    return A,A-p

if __name__=='__main__':
    print('\n\t\t\033[91mInterest Computer\t\033[0m\n')
    print('---'*20)
    parser=argparse.ArgumentParser()
    parser.add_argument('-p', action='store', dest='principle')
    parser.add_argument('-r',action='store',dest='rate')
    parser.add_argument('-t',action='store',dest='time')
    parsed=parser.parse_args()
    p,r,t=parsed.principle,parsed.rate,parsed.time
    p,r,t=float(p),float(r),int(t)
    print('\033[92mWith Simple Interest:\033[0m')
    print("\tAmount: %1f\tInterest: %2f"%simple_interest(p,r,t))
    print('---'*20)
    print("\033[93mWith Compound Interest:\033[0m")
    print("\tAmount: %1f\tInterest: %2f"%compound_interest(p,r,t))
    print("\nDifference:\033[94m %1f\033[0m"%(compound_interest(p,r,t)[0]-simple_interest(p,r,t)[0]))

