"""Escribir un programa que almacene en un lista los números primos comprendidos entre un
rango definido por el usuario"""
#Crear funcion que calcule primos
def es_primo(num):
    if num<=1:
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True
#Solicitarle el rango al usuario
l_menor=-1
while(l_menor<=0):
    l_menor=int(input("Introduzca el menor número del rango (debe ser mayor a cero): "))
    if l_menor<=0:
        print("Número invalido")
print()
l_mayor=l_menor-1
while( l_mayor<l_menor):
    l_mayor=int(input("Introduzca el mayor número del rango: "))
    if l_mayor<l_menor:
        print("Número invalido (debe ser mayor al número inferior)")
print()
#Analizar los primos
primos=[]
for i in range(l_menor,l_mayor+1):
    if es_primo(i)==True:
        primos.append(i)
print("Los números primos entre", l_menor,"y",l_mayor,"son: ")
print(primos)