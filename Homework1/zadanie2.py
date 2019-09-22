def pol(a):
    if 0 <= a <= 10000:
        if a//1000 == a % 10:
            if a % 1000//100 == a % 100//10:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("the number does not fit")


pol(567)