import random
i = random.randint(1,1000)
print(i)

#structuur

raads = 10
punten = 1

a = i + 50
b = i + 20
c = i - 50
d = i - 20
e = i + 51
f = i - 51


#programma 

while raads == 0 or punten < 20:
    print("Raad een nummer tussen 1 en 1000 , als u wilt stopOen dan scrijf 00")
    raad = int(input("Raad een nummer:"))
    if raad == i :
        punten += 1
        print("geraad! U heeft nu " , punten , "punt!")
        print("Nog een getal raden?")
        i = random.randint(1,1000)
        if punten == 20:
            break
        print(i)
    elif raad == 00:
        break
    elif raad > e :
        print("Uw raad is hoger! U mag",  raads , "raden")
        raads -= 1
        if raads == 0:
            break
    elif raad < f :
        print("Uw raad is lager! U mag",  raads , "raden")
        raads -= 1
        if raads == 0:
            break
    elif raad < a and raad > b :
        print("U bent warm! U mag",  raads , "raden")
        raads -= 1
        if raads == 0:
            break
    elif raad < b and raad > i :
        print("U bent heel warm! U mag", raads , "raden")
        raads -= 1
        if raads == 0:
            break
    elif raad  > c and raad < d :
        print("U bent warm! U mag",  raads , "raden")
        raads -= 1
        if raads == 0:
            break
    elif raad > d and raad < i :
        print("U bent heel warm!  U mag",  raads , "raden")
        raads -= 1
        if raads == 0:
            break
if punten == 20:
    print("Goed gedaan! u bent klaar , uw eindscore is" , punten)
elif raad == 00:
    print("U heeft gestopt met de game")
else:
    print("Helaas , U heeft verloren")

