def potencia(b,e):
  if e==0:
    return 1
  if e==1:
    return b
  else: 
    return b * potencia(b,e-1)
  
b=int(input("Escriba la base: "))
e=int(input("Escriba la potencia: "))

print(potencia(b,e))