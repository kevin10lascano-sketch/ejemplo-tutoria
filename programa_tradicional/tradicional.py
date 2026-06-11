def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area

# Solicitar al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área del círculo
area = calcular_area_circulo(radio)

# Mostrar el resultado
print(f"El área del círculo es: {area}")