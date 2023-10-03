import math

def sigma(times): #Named after sigma notation
    a = (0,)
    n=0
    for n in range(times):
        n+=1 #To calculate the number of times
        a = a + (n,)
        m = tuple([((((-1)**q)*math.factorial(6*q)*(545140134*q + 13591409))/(math.factorial(3*q)*((math.factorial(q)**3)*(640320**(3*q+(3/2)))))) for q in a]) # Tuple used to store a set of number, algorithm used is the Chudnovsky Algorithm (https://en.wikipedia.org/wiki/Chudnovsky_algorithm)
    x = sum(m) #The set fo numbers is added toghether
    return x
        
print((12*sigma(17))**(-1))