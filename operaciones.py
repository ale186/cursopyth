def porcentaje(numero, porcentaje = 13):
    resultado = numero * (porcentaje / 100)
    return resultado

def descuento(precio):
    descuento=0
    if precio > 100:
        descuento = porcentaje(precio, 15)
    else:
        descuento = porcentaje(precio,5)
    return descuento

def calcular(lista, funcion):
    total = 0
    for producto, precio in lista.items():
        total += funcion(precio)
    return total