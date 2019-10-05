def fn(s, w):
    lst1 = list(map(int, str(s)))
    lst2 = list(map(int, str(w)))
    lst1.reverse()
    lst2.reverse()
    if len(lst1) > len(lst2):
        lst2 = lst2 + [0 for j in range(len(lst1) - len(lst2))]
        print(lst1, lst2)
    elif len(lst1) < len(lst2):
        lst1 = lst1 + [0 for j in range(len(lst2) - len(lst1))]
        print(lst1, lst2)
    else:
        print(lst1, lst2)
    lst3 = [(lst1[0] + lst2[0]) % 10]
    for i in range(1, len(lst2)):
        lst3.append((lst1[i] + lst2[i]) % 10 + (lst1[i-1] + lst2[i-1])//10)
    if (lst1[len(lst2)-1] + lst2[len(lst2)-1])//10 != 0:
        lst3.append((lst1[len(lst2)-1] + lst2[len(lst2)-1])//10)
    lst3.reverse()
    return print(int("".join(map(str, lst3))))


print(fn(895, 2721))


def fn2(s, w):
    lst1 = list(map(int, str(s)))
    lst2 = list(map(int, str(w)))
    lst1.reverse()
    lst2.reverse()
    lst3 = []
    if len(lst1) > len(lst2):
        lst2 = lst2 + [0 for j in range(len(lst1) - len(lst2))]
    else:
        lst1 = lst1 + [0 for j in range(len(lst2) - len(lst1))]

    if s > w:
        for i in range(len(lst1)):
            if lst1[i] < lst2[i]:
                lst3.append(lst1[i] + 10 - lst2[i])
                lst1[i + 1] = lst1[i + 1] - 1
            else:
                lst3.append(lst1[i] - lst2[i])
        lst3.reverse()
        return print(int("".join(map(str, lst3))))
    else:
        for i in range(len(lst1)):
            if lst2[i] < lst1[i]:
                lst3.append(lst2[i] + 10 - lst1[i])
                lst2[i + 1] = lst2[i + 1] - 1
            else:
                lst3.append(lst2[i] - lst1[i])
        lst3.reverse()
        return print(int("".join(map(str, lst3))))


print(fn2(895, 2721))