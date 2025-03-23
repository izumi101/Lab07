n = int(input())
for i in range(0, n+1, 2):
    if i != n and i != 0:  
        print(f"{i},", end=" ")
    else:
        print(i)
