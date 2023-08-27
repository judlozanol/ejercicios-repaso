c =str(input("Ingrese palabra: "))
i=0
mayusculas=0
while i < len(c):
  letra = c[i]
  if letra.isupper() == True:
    mayusculas +=1
  i += 1

print("Total mayusculas: " ,mayusculas)