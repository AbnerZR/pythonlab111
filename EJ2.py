import math
#Utilizando los coeficientes (a, b, c) de una ecuación de segundo grado se pide mostrar
# la naturaleza de sus raíces

a, b, c = map(int, input("introducir a, b y c respectivamente: ").split())
x = math.sqrt((b**2) - (4*a*c))
x1 = ((-1*b) + x)/(2*a)
x2 = ((-1*b) - x)/(2*a)
print("la raiz 1 es: ", "{0:.4f}".format(x1))
print("la raiz 2 es: ", "{0:.4f}".format(x2))

#Abner Zabala Rios