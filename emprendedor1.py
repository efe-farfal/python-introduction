import math

# Solicitud de Inputs
p = int(input("precio de suscripcion:\n>"))
u = int(input("numero de usuarios:\n>"))
gt = int(input("gasto total:\n>"))

# cálculo de utilidades
utilidades = p * u - gt

# resultado utilidades
print(f'utilidades del proyecto: {utilidades}')