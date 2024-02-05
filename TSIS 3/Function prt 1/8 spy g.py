def spy_game(list):
    count=0
    for i in list:
        if i==0:
            count+=1
        elif i==7 and count>=2:
            return True
        elif i!=0 and i!=7:
            count+=0
        else:
            count=0
    return False    
        
print(spy_game([1,2,3,0,7,0,0,5,4,3,7]))
print(spy_game([1,2,4,0,0,7,5]) )#--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False
