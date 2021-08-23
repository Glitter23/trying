
def sum_of_multi():
    """multiples of 3 and 5 below 1000 and their sum"""
    """Multiples of  and 5"""
    l=[]
    for i in range(1,1000):
        
        if i%3==0 and i%5==0:
            l.append(i)
    
    sum_of_mul= sum(l)
    
    return sum_of_mul




if __name__ == '__main__':
    print(sum_of_multi())

