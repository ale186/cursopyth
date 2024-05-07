def porc(num,porcentaje):
    return (num*porcentaje/100)
c=porc(45,10)
print(c)
def porc2(num = 100, porcentaje = 10):
    return (num * porcentaje / 100)

def porcentajeLista(lista, porcentaje=10):
    lista1=[]
    for numero in lista:
        lista1.append(porc(numero,porcentaje))
    return lista1
lista=[45,68,97,68,100,25,64]
listaporcentual=porcentajeLista(lista)
print(lista)
print(listaporcentual)