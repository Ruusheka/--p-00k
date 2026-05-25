n=5
for i in range(1,n+1):
    
    for j in range(1,n-i+2):
        print(j,end="")
    
    for s in range(2*(i-1)):
        print("*",end="")
    
    for k in range(n-i+1,0,-1):
        print(k,end="")

    print("")
    