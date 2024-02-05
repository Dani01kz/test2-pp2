def revers(ls):
    ls.reverse()
    x=" ".join(ls)
    
    return x
    
        
str=input().split()
x=revers(str)
print(x)