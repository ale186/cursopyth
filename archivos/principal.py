import operaciones as op
ruta = 'ventas.csv'
nueva_venta = {
    'id': 0,
    'codigo_cliente': 10000,
    'cliente': 'jose perez',
    'producto': 'Papas Fritas',
    'precio': 68,
    'descuento': '',
    'iva':''
}
#op.registrar_csv(nueva_venta, ruta)

operacion = input("¿Quieres añadir?: ")
operacion= operacion.lower()
while operacion != "terminar" or operacion != "no":
    if operacion == "si" or operacion=="nuevo":
        nuevaventa = {}
        nuevaventa['id']=0
        nuevaventa['codigo_cliente'] = input("ingrese el codigo de cliente: ")
        nuevaventa['cliente'] = input("ingrese su nombre: ")
        nuevaventa['producto'] = input("ingrese el producto: ")
        nuevaventa['precio'] = input("ingrese el precio: ")
        print(nuevaventa)
        op.registrar_csv(nuevaventa, ruta)
        operacion = input("¿Quieres añadir?: ")
        operacion= operacion.lower()
    if operacion == "terminar" or operacion == "no":
        break
        

