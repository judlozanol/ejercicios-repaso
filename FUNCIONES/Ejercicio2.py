def resta_doble_cuadrado(numero):
    resultado = numero**2 - (2 * numero)
    return resultado


numero = float(input("Ingrese un número: "))


resultado = resta_doble_cuadrado(numero)


print("El resultado de restar el doble de", numero, "a su cuadrado es:", resultado)
