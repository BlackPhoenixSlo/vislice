import math
def pra(n):
    for i in range (2,(int)(math.sqrt(n))):
        if (n%i==0):
            return False
    return True
def izpisi():
    for i in range (2,200):
        if (pra(i)):
            print(i)
