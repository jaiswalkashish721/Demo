n=int(input("enter rows"))
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("*",end="")
    print()