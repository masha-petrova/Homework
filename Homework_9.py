# задание 1
def fn1(a):
    a = list(map(int,str(a)))
    if len(a) == 1:
        return int(''.join(str(e) for e in a))
    else:
        return fn1(sum(a))

print(fn1(1238))


# задание 2
def A(m,n):
    if m == 0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))

print(A(1,3))


# задание 3
def fn3(a, c=[]):
    if a//10 == 0:
        c.append(a)
        return c
    else:
        c.append(a % 10)
        return fn3(a//10,c)

print(fn3(1238))

# задание 4
k=[]
def f4(a):
    if a==0:
        k.reverse()
        return int(''.join(str(e) for e in k))
    else:
        k.append(a%2)
        return f4(a//2)

print(f4(111))


# задание 5
def f5(n, k=2):
    if k > (n / 2):
        return print(n)
    elif n % k == 0:
        return f5(n / k, k)
    else:
        return f5(n, k+1)

print(f5(39,2))