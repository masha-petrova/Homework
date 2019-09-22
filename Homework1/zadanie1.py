def f10(day, hour):
    if day % 2 == 0:
        if hour >= 21:
            return print("right")
        elif hour < 19:
            return print("left")
        else:
            return print("both")
    else:
        if hour >= 21:
            return print("left")
        elif hour < 19:
            return print("right")
        else:
            return print("both")


print(f10(23, 12))