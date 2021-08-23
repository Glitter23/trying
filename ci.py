#Compounnd Interest
def ci(t,p,r):
    A = p *((1+(r/100))**t)
    
    CI = A - p
    return CI

z=ci(4,50000,4)
print(z)

#amount
def amount(p,r,t):
    A = p *((1+(r/100))**t)
    return A

#rate 
def rate(A,p,t):
    r=((A/p)**(1/t)) - 1
    return r

k=rate(90000,45000,2)
print(k)
