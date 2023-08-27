""" Escribir un programa que lea un tiempo en horas, minutos y segundos y empiece a
cronometrar el tiempo mostrándolo en pantalla hasta llegar al limite leído al inicio.
"""
import time

def avanzar_seg(segundos):
    segundos+=1
    if segundos==60:
        segundos=0
    return segundos

def avanzar_min(minutos):
    minutos+=1
    if minutos==60:
        minutos=0
    return minutos
def avanzar_hora(horas):
    horas+=1
    if horas==25:
        horas=0
    return horas

horas_f,minutos_f,segundos_f=str(input("Ingrese las horas, minutos y segundos que desea contar respectivamente separados por un espacio (hh mm ss):\n")).split(" ")
horas_f=int(horas_f)
minutos_f=int(minutos_f)
segundos_f=int(segundos_f)
segundos_f= segundos_f + (horas_f*3600) + (minutos_f*60)
input("\nPresione enter para iniciar el conteo...")
seg=0
min=0
hora=0
for i in range(segundos_f+1):
    if seg//10==0:
        if min//10==0:
            if hora//10==0:
                print("0"+str(hora)+":0"+str(min)+":0"+str(seg))
            else:
                print(str(hora)+":0"+str(min)+":0"+str(seg))
        else:
            if hora//10==0:
                print("0"+str(hora)+":"+str(min)+":0"+str(seg))
            else:
                print(str(hora)+":"+str(min)+":0"+str(seg))
    else:
        if min//10==0:
            if hora//10==0:
                print("0"+str(hora)+":0"+str(min)+":"+str(seg))
            else:
                print(str(hora)+":0"+str(min)+":"+str(seg))
        else:
            if hora//10==0:
                print("0"+str(hora)+":"+str(min)+":"+str(seg))
            else:
                print(str(hora)+":"+str(min)+":"+str(seg))
    time.sleep(1)
    seg=avanzar_seg(seg)
    if seg==0:
        min=avanzar_min(min)
        if min==0:
            hora=avanzar_hora(hora)
print("\n\tCONTEO FINALIZADO\n")
print("\t◥------◥\n\tl ● ▄ ◉ l ѠOOƑ!\n\tl‿/ʊ\‿l\n\tl══o══l\n\t︳ ︳︳ l⊃\n\tఋ︵ ఋ\n")

