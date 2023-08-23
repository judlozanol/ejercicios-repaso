def calcular_potencia(base, exponente):
    potencia = 1
    
    if exponente < 0:
        base = 1 / base
        exponente = -exponente
    
    for _ in range(exponente):
        potencia *= base
    
    return potencia

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = calcular_potencia(base, exponente)


print("El resultado de", base, "elevado a la", exponente, "es:", resultado)
