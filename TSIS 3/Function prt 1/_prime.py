def is_prime(x):
    if x<2:
        return 0 
    for i in range(2,int(x/2)+1):
        if x%i==0:
            return False
    return True
        
Numbers=input().split()
prime_list=[]
for i in Numbers:
    if is_prime(int(i)):
        prime_list.append(i)
        
print(prime_list)

