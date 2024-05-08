productos = {
    "arroz": 58,
    "gaseosas": 50,
    "trigo": 25,
    "arina": 100
}
def porcentaje(numero, porcentaje):
    resultado = numero * (porcentaje / 100)
    return resultado

def descuento(precio):
    descuento=0
    if precio > 100:
        descuento = porcentaje(precio, 15)
    else:
        descuento = porcentaje(precio,5)
    return descuento
#print(descuento(10))

def calcular(lista, funcion):
    total = 0
    for producto, precio in lista.items():
        total += funcion(precio)
    return total

iva = calcular(productos, porcentaje)
print(f"Iva total: {iva}")
total = calcular(productos, descuento)
print(f"Descuento tota: {total}")


