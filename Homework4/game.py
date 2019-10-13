# Создание классов
import random


class Warrior:
    def __init__(self, newName):
        self.name = newName
        self.health = random.randint(100, 150)
        self.Attack_Power = random.randint(20, 30)

    def getHealth(self):
        return print("Здоровье игрока", self.name, "=", self.health)

    Attack_Power = random.randint(20, 30)

    def getPower(self):
        return print("Сила атаки игрока", self.name, "=", self.Attack_Power)

    def damage(self, Attack_Power):
        self.health = self.health - Attack_Power
        if self.health > 0:
            return print(self.name, "получил", Attack_Power, "урона. Осталось", self.health, "здоровья.")
        else:
            return print(self.name, "получил", Attack_Power, "урона и погиб.")


class Warrior_shield(Warrior):
    def __init__(self, newName):
        Warrior.__init__(self, newName)
        self.protection = random.randint(5, 10)

    def getProtection(self):
        return print("Защита игрока", self.name, "=", self.protection)

    def damage(self, Attack_Power):
        self.health = self.health - Attack_Power + self.protection
        if self.health > 0:
            return print(self.name, "получил", Attack_Power - self.protection, "урона. Осталось", self.health,
                         "здоровья.")
        else:
            return print(self.name, "получил", Attack_Power - self.protection, "урона и погиб.")


class Warrior_expert(Warrior):
    def Attack(self):
        if random.randint(1, 5) == 1:
            return self.Attack_Power * 2
        else:
            return self.Attack_Power


# Задача 1
Ron = Warrior("Ron")
Ron.getPower()

Harry = Warrior_shield("Harry")
Harry.getPower()

Draco = Warrior_expert("Draco")
Draco.Attack()

# Задача 2
Ron2 = Warrior("Ron2")
Harry2 = Warrior_shield("Harry2")
Draco2 = Warrior_expert("Draco2")

print("Бой между", Ron.name, "и", Harry2.name)
i = 1
while Ron.health > 0 and Harry2.health > 0:
    if i % 2 == 1:
        Harry2.damage(Ron.Attack_Power)
    else:
        Ron.damage(Harry2.Attack_Power)
    i += 1

print("Бой между", Ron2.name, "и", Draco.name)
i = 1
while Ron2.health > 0 and Draco.health > 0:
    if i % 2 == 1:
        Draco.damage(Ron2.Attack_Power)
    else:
        Ron2.damage(Draco.Attack())
    i += 1

print("Бой между", Harry.name, "и", Draco2.name)
i = 1
while Harry.health > 0 and Draco2.health > 0:
    if i % 2 == 1:
        Draco2.damage(Harry.Attack_Power)
    else:
        Harry.damage(Draco2.Attack())
    i += 1


# Задача 3
wn1 = Warrior("wn1")
wn2 = Warrior("wn2")
wn3 = Warrior("wn3")
wn4 = Warrior("wn4")
wn5 = Warrior_shield("wn5")
wn6 = Warrior_shield("wn6")
wn7 = Warrior_shield("wn7")
wn8 = Warrior_shield("wn8")
wn9 = Warrior_expert("wn9")
wn10 = Warrior_expert("wn10")
a1=[wn1,wn2,wn3,wn4,wn5,wn6,wn7,wn8,wn9,wn10]
wn11 = Warrior("wn11")
wn12 = Warrior("wn12")
wn13 = Warrior("wn13")
wn14 = Warrior("wn14")
wn15 = Warrior_shield("wn15")
wn16 = Warrior_shield("wn16")
wn17 = Warrior_shield("wn17")
wn18 = Warrior_shield("wn18")
wn19 = Warrior_expert("wn19")
wn20 = Warrior_expert("wn20")
a2=[wn11,wn12,wn13,wn14,wn15,wn16,wn17,wn18,wn19,wn20]

i=1
while len(a1)>0 and len(a2)>0:
    if i % 2 == 1:
        v1 = random.randint(0, len(a1)-1)
        v2 = random.randint(0, len(a2)-1)
        if type(a1[v1]) is Warrior_expert:
            a2[v2].damage(a1[v1].Attack())
        else:
            a2[v2].damage(a1[v1].Attack_Power)
        if a2[v2].health<0:
             del a2[v2]
    else:
        v1 = random.randint(0, len(a1) - 1)
        v2 = random.randint(0, len(a2) - 1)
        if type(a2[v2]) is Warrior_expert:
            a2[v2].Attack()
            a1[v1].damage(a2[v2].Attack())
        else:
            a1[v1].damage(a2[v2].Attack_Power)
        if a1[v1].health<0:
            del a1[v1]
    i+=1
if i%2==1:
    print("Победила армия 2")
else:
    print("Победила армия 1")
