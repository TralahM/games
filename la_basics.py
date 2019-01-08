#!/data/data/com.termux/files/usr/bin/env python
import numpy as np
M=np.matrix([[3,5],[8,13]])
u=np.array([[1],[2]])
v=np.array([[-1],[-4]])
print("Vector u: %s,\nVector v: %s"%(np.array2string(u),np.array2string(v)))
print("Matrix M: \n%s"%(np.array2string(M,separator=' ')))
print("Checking if Mu+Mv=M(u+v)")
print(M*u+M*v,'=\t',M*(u+v))
print(M*u+M*v==M*(u+v))


