##Moving Median

arr=[1,2,32,1,2,4,5,6,7,6,4,3,32,3,3,3,3]
n=6

l=[]
for i in range(len(arr)-6):
    j=arr[i:i+6]
    k=sorted(j)
    su=sum(k)
    l.append(su)


print(l)




