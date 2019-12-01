class ApiException(Exception):
    pass
class ApiException2(Exception):
    pass

def position():
    try:
        a = str(input("Введите позицию белого короля, белой ладьи и черного короля:"))
        b = a.split()
        alf = "abcdefgh"
        kw0 = b[0][0]
        lw0 = b[1][0]
        kb0 = b[2][0]
        kw1 = alf.find(kw0)
        lw1 = alf.find(lw0)
        kb1 = alf.find(kb0)
        kw2 = int(b[0][1])
        lw2 = int(b[1][1])
        kb2 = int(b[2][1])
        if 0 > kw2 or kw2 > 8 or 0 > lw2 or lw2 > 8 or 0 > kb2 or kb2 > 8:
            raise ApiException("action failed")
        if alf.find(kw0) == -1 or alf.find(lw0) == -1 or alf.find(kb0) == -1:
            raise ApiException2("action failed")
        if kb2 == lw2:
            if kb1 == kw1:
                if kb2 == kw2 + 2 or kb2 == kw2 - 2:
                    print("Checkmate")
            else:
                print("Check")
        elif kb1 == lw1:
            if kb2 == kw2:
                if kb1 == kw1 + 2 or kb1 == kw1 - 2:
                    print("Checkmate")
            else:
                print("Check")
        elif kb2 != lw2 and kb1 != lw1:
            if kb1 == 1 and kb2 == 8:
                if kw1 == "a" and kw2 == 6 and lw0 == "b":
                    print("Stalemate")
                if kw2 == 8 and kw0 == "c" and lw2 == 7:
                    print("Stalemate")
            elif kb0 == "a" and kb2 == 1:
                if kw0 == "a" and kw2 == 3 and lw0 == "b":
                    print("Stalemate")
                if kw2 == 1 and kw0 == "c" and lw2 == 2:
                    print("Stalemate")
            elif kb0 == "h" and kb2 == 8:
                if kw0 == "h" and kw2 == 6 and lw0 == "g":
                    print("Stalemate")
                if kw2 == 8 and kw0 == "f" and lw2 == 7:
                    print("Stalemate")
            elif kb0 == "h" and kb2 == 1:
                if kw0 == "h" and kw2 == 3 and lw0 == "g":
                    print("Stalemate")
                if kw2 == 1 and kw0 == "f" and lw2 == 2:
                    print("Stalemate")
            if kb2 == kw2:
                if kb1 == kw1 + 1 or kb1 == kw1 - 1:
                    print("Strange")
            if kb2 == kw2 + 1:
                if kb1 == kw1 or kb1 == kw1 + 1 or kb1 == kw1 - 1:
                    print("Strange")
            if kb2 == kw2 - 1:
                if kb1 == kw1 or kb1 == kw1 + 1 or kb1 == kw1 - 1:
                    print("Strange")
        else:
            print("Normal")
    except ApiException:
        print("параметры не валидны")
    except ApiException2:
        print("параметры не валидны")


position()