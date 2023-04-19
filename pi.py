import math
import decimal

def sigma(times):
    a = (0,)
    n=0
    for n in range(times):
        n+=1
        a = a + (n,)
        m = tuple([((((-1)**q)*math.factorial(6*q)*(545140134*q + 13591409))/(math.factorial(3*q)*((math.factorial(q)**3)*(640320**(3*q+(3/2)))))) for q in a])
    x = sum(m)
    return x
        
print((12*sigma(17))**(-1))