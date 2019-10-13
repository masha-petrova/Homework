# Я не понимаю, почему оно не работает. Я пыталась.

class Room:
    def __init__(self, l, s, h):
        self.l = l
        self.s = s
        self.h = h
        self.doors = []
        self.windows = []
        self.S = 2*self.h*(self.s+self.l)
    def testwin(self, b):
        if b.s > self.l or b.h+b.ot > self.h or b.s > self.s or b.s*b.h > self.l*self.h or b.s*b.h > self.s*self.h:
            return 0
    def testdo(self, b):
        if b.s > self.l or b.s > self.s or b.s*b.h > self.l*self.h or b.s*b.h > self.s*self.h:
            return 0
    def wallp(self,b):
        if b.o == 1:
            self.S = self.S - b.s*b.h
            return self.S
        else:
            self.S = self.S
            return self.S
    def wallp2(self, b):
        self.S = self.S - b.s*b.h


class Frame:
    def __init__(self, s, h):
        self.s = s
        self.h = h


class Door(Frame):
    def __init__(self, s, h, o):
        Frame.__init__(self, s, h)
        self.o = o

class Window(Frame):
    def __init__(self, s, h, ot):
        Frame.__init__(self, s, h)
        self.ot = ot


def fn():
    l = int(input())
    s = int(input())
    h = int(input())
    r = Room(l,s,h)
    n = int(input())
    for i in range(1, n + 1):
        h = input()
        s = input()
        o = input()
        if r.testdo(Door(h, s, o)) == 0:
            return r.wallp(Door(h, s, o))
    n2 = int(input())
    for i in range(n2 + 1):
        h = input()
        s = input()
        ot = input()
        if r.testwin(Window(h, s, ot)) == 0:
            return r.wallp2(Window(h, s, ot))
    print("Площадь обоев = ", r.S)

fn()