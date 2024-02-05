def set(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    return a
x=input().split()
print(set(x))
