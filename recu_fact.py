def dec(n):
    if n == 1:
        return 1
    else:
        return n*dec(n-1)

n = int(input("enter no"))
f=dec(n)
print(f)


