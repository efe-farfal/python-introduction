import math

# Solicitud de Inputs
p = float(input("precio de suscripcion:\n>"))
u = float(input("numero de usuarios:\n>"))
gt = float(input("gasto total:\n>"))
ua = float(input("utilidades anteriores:\n>"))

# cálculo de utilidades
utilidades = p * u - gt
razon = ua/utilidades

# resultado utilidades
print(f'utilidades del proyecto: {razon:.2f}')