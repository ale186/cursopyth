lista=[1,1,2,3,3,1,4,8,3]
lista_unica=[]
for numero in lista:
    print(numero)
for i in range(len(lista)):
    print(lista[i])
for numero in lista:
    if numero not in lista_unica:
        lista_unica.append(numero)
print(lista_unica)
lista_unica2= set(lista)
print(lista_unica2)
print(type(lista_unica))
print(type(lista_unica2))
#=============================
grupo1 = set("abracadabra")
grupo2 = set("alacazam")
print(grupo1, grupo2)
print(grupo1 - grupo2)
print(grupo2 - grupo1)
print(grupo2 | grupo1)
print(grupo1 & grupo2)
print(grupo1 ^ grupo2)