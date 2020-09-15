# Dados 3 valores (horas, minutos y segundos) se pide sumar un segundo.

x, y, z = map(int, input("introducir horas, minutos y segundos respectivamente: ").split())
if (x >= 0) and (x <= 23) and (y >= 0) and (y <= 59) and (z >= 0) and (z <= 59):
    z = z + 1
    if z == 60:
        z = 00
        y = y + 1
        if y == 60:
            y = 00
            x = x + 1
            if x == 24:
                x = 00
                print(x, ":", y, ":", z)
            else:
                print(x, ":", y, ":", z)
        else:
            print(x, ":", y, ":", z)
    else:
        print(x, ":", y, ":", z)
else:
    print("datos incorrectos!!!")

#Abner Zabala Rios