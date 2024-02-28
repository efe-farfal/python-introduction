# librería math
import math

# datos
radio = int(input("Ingrese el radio en kilometros:\n>"))
gravedad = float(input("Ingrese la constante g:\n>"))

# cálculo
radio = radio * 1000
ve = math.sqrt(2*gravedad*radio)

# resultado calculo
print(f'La velocidad del escape es: {ve}[m/s]')
