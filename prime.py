##prime numbers program.

from itertools import count

x=[]

def afunc(strArr):
    l=[]
    d={}
    sum=0
    for i,j in enumerate(strArr):
        if j[0] in d.keys():
            d[j[0]]=int(d[j[0]])+int(j[2:])
        else:
            d[j[0]]=j[2:]


    print(d)
        

        
            


    
    

   



if __name__=="__main__":
    x=['X:-1','X:-4','Y:3','X:5','Y:-1']
    
    afunc(x)

