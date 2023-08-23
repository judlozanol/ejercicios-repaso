"""Crear un módulo de funciones aritméticas que realicen las operaciones de suma, resta,
multiplicación, división y potencia de enteros, escribir un programa que importe este
módulo y use estas funciones para operar con números capturados desde el teclado."""
import aritmetica
import os
import time
#Funcion que limpia la consola
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
         os.system ("cls")
#Funcion para cuando la condición introducida no es valida
def condicionInvalida():
    print("Condición invalida") 
    time.sleep(1)
    borrarPantalla()
#Linea principal
borrarPantalla()
condition=6
while(condition>=6 or condition<=0):
    print("Introduzca el número de la operación que desea realizar:\n\tSuma (1)\n\tResta (2)\n\tMultiplicación (3)\n\tDivisión (4)\n\tPotencia de enteros (5)\n")
    try:
        condition=int(input())
        if condition>=6 or condition<=0 :
            condicionInvalida()
    except ValueError:
        condicionInvalida()