"""Escribir un programa que calcule el número de horas, minutos y segundos que hay en un
valor x de segundos indicados por el usuario."""

segundos= int(input("Introduzca un valor x de segundos: "))
horas=segundos//3600
minutos=(segundos%3600)//60
seg=(segundos%3600)%60
print("En",segundos,"segundos hay",horas,"hora(s),",minutos,"minutos(s) y", seg,"segundos.")