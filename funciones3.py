productos = {
    "arroz": 58,
    "gaseosas": 50,
    "trigo": 25,
    "arina": 100
}

def porcentaje(numero, porcentaje):
    resultado = numero * (porcentaje / 100)
    return resultado

def iva(diccionario):
    iva=0
    for clave, valor in diccionario.items():
        iva=iva + porcentaje(valor,13)
    return (iva)
print(iva(productos))