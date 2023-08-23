inicio = int(input("Ingrese el número inicial del rango: "))
fin = int(input("Ingrese el número final del rango: "))

suma = 0

for i in range(inicio, fin+1):
    suma += i
  
print("La suma de los números en el rango es:", suma)
