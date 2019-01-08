#!/data/data/com.termux/files/usr/bin/env python

""" The Problem of allocating resources
returning balances of 1000, 500, 200, 100, 50, 40, 20, 10, 5, 1
denominations.
optimizing the parameters to the eqn:
    1000x1+500x2+200x3+100x4+50x5+40x6+20x7+10x8+5x9+1x10= A desired outcome Y
    where x€Xi i={1..10} x>=0 i.e non-negative

"""
denoms=[1000,500,200,100,50,40,20,10,5,1]

print(denoms,'\n',sum(denoms),'\n',sum(denoms)/len(denoms),'\n',len(denoms))
