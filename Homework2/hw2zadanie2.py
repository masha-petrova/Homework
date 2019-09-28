def fn2(n):
    tyda = 0
    obratno = 0
    for i in range(1, n + 1, 2):
        tyda = tyda + 1 / i
    for i in range(2, n + 1, 2):
        obratno = obratno + 1 / i
    home = tyda - obratno
    total = tyda + obratno
    return print('Общий путь =', total, 'Расстояние от дома =', home)


print(fn2(3))