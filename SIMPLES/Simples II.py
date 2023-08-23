"""Escribir un programa que calcule el área de un rectángulo a partir de sus coordenadas x1, y1,
x2, y2."""
def valor_absoluto(num):
    if num>=0:
        return num
    else:
        return -1 *num

print("\tEL AREA DE UN RECTANGULO")
x1= int(input("Introduzca el valor en x del punto 1: "))
y1= int(input("Introduzca el valor en y del punto 1: "))
x2= int(input("Introduzca el valor en x del punto 2: "))
y2= int(input("Introduzca el valor en y del punto 2: "))
area= valor_absoluto(x2-x1)* valor_absoluto(y2-y1)
print("El area del rectangulo introducido es de", area,"unidades cuadradas")