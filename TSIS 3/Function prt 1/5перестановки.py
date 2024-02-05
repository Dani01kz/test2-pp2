def all_var(str2,x=0):
    if(x==len(str2)):
        print("".join(str2))
        return 
    for i in range(x,len(str2)):
        str2[i],str2[x]=str2[x],str2[i]
        all_var(str2,x+1)
        str2[i], str2[x] = str2[x], str2[i]
        
         
    

str=input("Enter a string:")
str2=list(str)
all_var(str2)