def f(n):
    print(n, end=" ")
    if(n<=1) :
        return 0
    else:
        f(n-1)
n = int(input())
f(n)
