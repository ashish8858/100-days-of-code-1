n=int(input("Enter a number"))
i=1
print("Factor : ")
while i<=n:
    if n%i==0:
        print(i,end=" ")
    i=i+1