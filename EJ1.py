# Ingrese un tiempo X que estará representado en segundos, luego ingrese el tiempo que tomará en realizarse
# una tarea Z representado en segundos, minutos y horas. Se pide verificar si con el tiempo X se puede
# finalizar la tarea Z.

x = int(input("ingrese el tiempo dado (en segundos) para realizar la tarea: "))
z1, z2, z3 = map(float, input("ingrese el tiempo en el que se tardará en "
                     "resolver la tarea en segundos, minutos y horas respectivamente : ").split())
if z1 <= x:
    print("el tiempo dado alcanza para realizar la tarea")
else:
    print("el tiempo dado No alcanza para realizar la tarea")

#Abner Zabala Rios