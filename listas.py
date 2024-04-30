impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(impares[4:])
print(impares[:8])
print(impares[4::8])
impares.reverse()
print(impares)
desordenado = [5, 2, 3, 8, 46, 54, 1]
desordenado.sort()
print(desordenado)

n=int(input("ingresa un número entero: "))
if n%2 == 0:
    print(f"El número {n} es par")
else:
    print(f"El número {n} es impar")
