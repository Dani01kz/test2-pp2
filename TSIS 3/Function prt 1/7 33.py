def has_33(list):
    x=0
    while(x<len(list)-1):
        
        if list[x]==3 and list[x+1]==3:
            return True
        x+=1
    return False        
            
print(has_33([1,2,3,4,5]))
print(has_33([1,2,3,3,5]))
print(has_33([1,2,3,4,3]))
print(has_33([3,3,2,3,4]))