def validar_binario(num):
    if num=="":
        return False
    else:
        lista = list(str(num))
        a= len(lista)
        i=0
        while i<a:
            if lista[i]=="0":
                lista.remove("0")
                i-=1
            elif lista[i]=="1":
                lista.remove("1")
                i-=1
            i+=1
            a=len(lista)
        if len(lista)==0:
            return True
        else:
            return False
    
def validar_decimal(num):
    if num=="":
        return False
    else:
        lista = list(str(num))
        a= len(lista)
        i=0
        while i<a:
            if lista[i]=="0":
                lista.remove("0")
                i-=1
            elif lista[i]=="1":
                lista.remove("1")
                i-=1
            elif lista[i]=="2":
                lista.remove("2")
                i-=1
            elif lista[i]=="3":
                lista.remove("3")
                i-=1
            elif lista[i]=="4":
                lista.remove("4")
                i-=1
            elif lista[i]=="4":
                lista.remove("4")
                i-=1
            elif lista[i]=="5":
                lista.remove("5")
                i-=1
            elif lista[i]=="6":
                lista.remove("6")
                i-=1
            elif lista[i]=="7":
                lista.remove("7")
                i-=1
            elif lista[i]=="8":
                lista.remove("8")
                i-=1
            elif lista[i]=="9":
                lista.remove("9")
                i-=1    
            i+=1
            a=len(lista)
        if len(lista)==0:
            return True
        else:
            return False
        
def validar_octal(num):
    if num=="":
        return False
    else:
        lista = list(str(num))
        a= len(lista)
        i=0
        while i<a:
            if lista[i]=="0":
                lista.remove("0")
                i-=1
            elif lista[i]=="1":
                lista.remove("1")
                i-=1
            elif lista[i]=="2":
                lista.remove("2")
                i-=1
            elif lista[i]=="3":
                lista.remove("3")
                i-=1
            elif lista[i]=="4":
                lista.remove("4")
                i-=1
            elif lista[i]=="4":
                lista.remove("4")
                i-=1
            elif lista[i]=="5":
                lista.remove("5")
                i-=1
            elif lista[i]=="6":
                lista.remove("6")
                i-=1
            elif lista[i]=="7":
                lista.remove("7")
                i-=1  
            i+=1
            a=len(lista)
        if len(lista)==0:
            return True
        else:
            return False
    
def validar_hexadecimal(num):
    if num=="":
        return False
    else:
        lista = list(str(num))
        a= len(lista)
        i=0
        while i<a:
            if lista[i]=="0":
                lista.remove("0")
                i-=1
            elif lista[i]=="1":
                lista.remove("1")
                i-=1
            elif lista[i]=="2":
                lista.remove("2")
                i-=1
            elif lista[i]=="3":
                lista.remove("3")
                i-=1
            elif lista[i]=="4":
                lista.remove("4")
                i-=1
            elif lista[i]=="4":
                lista.remove("4")
                i-=1
            elif lista[i]=="5":
                lista.remove("5")
                i-=1
            elif lista[i]=="6":
                lista.remove("6")
                i-=1
            elif lista[i]=="7":
                lista.remove("7")
                i-=1
            elif lista[i]=="8":
                lista.remove("8")
                i-=1
            elif lista[i]=="9":
                lista.remove("9")
                i-=1
            elif lista[i]=="A":
                lista.remove("A")
                i-=1
            elif lista[i]=="B":
                lista.remove("B")
                i-=1
            elif lista[i]=="C":
                lista.remove("C")
                i-=1
            elif lista[i]=="D":
                lista.remove("D")
                i-=1
            elif lista[i]=="E":
                lista.remove("E")
                i-=1
            elif lista[i]=="F":
                lista.remove("F")
                i-=1  
            i+=1
            a=len(lista)
        if len(lista)==0:
            return True
        else:
            return False




if validar_hexadecimal("AB76Z")==True:
    print("si")
else:
    print("no")
