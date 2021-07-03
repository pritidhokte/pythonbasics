no=int(input("how many digit"))
n1=0
n2=1
count=2
print(n1 ,n2 ,end="")
while count<no:
    n3=n1+n2
    print(n3 ,end="")
    n1 = n2
    n2 = n3
    count+= 1