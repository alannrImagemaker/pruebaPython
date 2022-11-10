
numero = 4
minimo = 5
maximo = 3

def recortar():
    if numero  < minimo:
        print("limite inferior",minimo)
    if minimo  > maximo:
        print("limite superior",maximo)
    if numero > minimo or numero > maximo:
        print("sin cambios numero",numero)

recortar()