import operaciones
productos= {
    'cereales': 58,
    'carne': 150,
    'gaseosas': 84,
    'arroz': 259,
    'papel': 78,
    'maletas': 598,
    'tomate': 65,
    'cebolla': 35,
    'mesa': 567
}

iva = operaciones.calcular(productos, operaciones.porcentaje)
desc = operaciones.calcular(productos, operaciones.descuento)

print(f'iva: {iva} \ndesc: {desc}')