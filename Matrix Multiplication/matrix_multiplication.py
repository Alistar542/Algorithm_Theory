from cmath import inf
import numpy as np


def matrix_chain_order(p):

    n = len(p) - 1
    m = np.zeros([n,n])
    s = np.zeros([n-1, n])

    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j = i+l-1
            m[i,j] = 0
            for k in range(i,j):
                q = m[i,k] + m[k+1,j] + p[i]* p[k+1] * p[j+1]
                # The check is made to greater than to find the
                # the most expensive way
                if q > m[i,j]: 
                    m[i,j] = q
                    s[i,j] = k+1

    print("M matrix")
    print(m)
    print("Cut matrix")
    print(s)
    return [m,s]

p = [30,35,15,5,10,25]
matrix_chain_order(p)




                




