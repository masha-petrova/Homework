def f1(a):
    a.reverse()
    for j in reversed(range(len(a))):
        if a.count(a[j]) > 1:
            a.remove(a[j])
    a.reverse()
    return print(a)


b = [2, 'cat', 7, 2, 9, 'cat', 7, 42]
print(f1(b))