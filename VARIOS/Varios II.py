""" Modifique el ejercicio anterior para que el conteo se haga hacia atrás desde el tiempo leído
hasta cero"""
import time

def retroceder_seg(segundos):
    segundos-=1
    if segundos==-1:
        segundos=59
    return segundos

def retroceder_min(minutos):
    minutos-=1
    if minutos==-1:
        minutos=59
    return minutos
def retroceder_hora(horas):
    horas-=1
    return horas

horas_i,minutos_i,segundos_i=str(input("Ingrese las horas, minutos y segundos desde donde desea iniciar el conteo regresivo respectivamente separados por un espacio (hh mm ss):\n")).split(" ")
horas_i=int(horas_i)
minutos_i=int(minutos_i)
segundos_i=int(segundos_i)
tiempo_i= segundos_i + (horas_i*3600) + (minutos_i*60)
input("\nPresione enter para iniciar el conteo...")
while tiempo_i>=0:
    if segundos_i//10==0:
        if minutos_i//10==0:
            if horas_i//10==0:
                print("0"+str(horas_i)+":0"+str(minutos_i)+":0"+str(segundos_i))
            else:
                print(str(horas_i)+":0"+str(minutos_i)+":0"+str(segundos_i))
        else:
            if horas_i//10==0:
                print("0"+str(horas_i)+":"+str(minutos_i)+":0"+str(segundos_i))
            else:
                print(str(horas_i)+":"+str(minutos_i)+":0"+str(segundos_i))
    else:
        if minutos_i//10==0:
            if horas_i//10==0:
                print("0"+str(horas_i)+":0"+str(minutos_i)+":"+str(segundos_i))
            else:
                print(str(horas_i)+":0"+str(minutos_i)+":"+str(segundos_i))
        else:
            if horas_i//10==0:
                print("0"+str(horas_i)+":"+str(minutos_i)+":"+str(segundos_i))
            else:
                print(str(horas_i)+":"+str(minutos_i)+":"+str(segundos_i))
    if tiempo_i==0:
        print("\n\tCONTEO FINALIZADO\n")
        print("\t◥------◥\n\tl ● ▄ ◉ l ѠOOƑ!\n\tl‿/ʊ\‿l\n\tl══o══l\n\t︳ ︳︳ l⊃\n\tఋ︵ ఋ\n")
    time.sleep(1)
    segundos_i=retroceder_seg(segundos_i)
    if segundos_i==59:
        minutos_i=retroceder_min(minutos_i)
        if minutos_i==59:
            horas_i=retroceder_hora(horas_i)
    tiempo_i-=1

