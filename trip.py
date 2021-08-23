##hcf program
def hcf(a,b):
    i=1
    gcd=0
    while(i<=a and i<=b):
        if a%i==0 and b%i==0:
            gcd=i
        i = i +1
    return gcd

c=hcf(200,10)
print(c)
