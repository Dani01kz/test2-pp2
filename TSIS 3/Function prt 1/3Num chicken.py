def solve(numheads,numlegs):
    
    for chickens in range(numheads+1):
        rabbits=numheads-chickens
        if chickens*2+rabbits*4== numlegs:
            print(f"Rabbits:{rabbits}\nChickens: {chickens}")
            return 0
    print("No solution")
        
x=input()  
y=input()
solve(int(x),int(y))