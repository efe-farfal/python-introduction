import math

# Solicitud de Inputs
p = int(input("precio de suscripcion:\n>"))
u = int(input("numero de usuarios:\n>"))
up = int(input("numero de usuarios premium:\n>"))
gt = int(input("gasto total:\n>"))

# cálculo de utilidades
preciopremium = 1.5 * p
up *= preciopremium
utilidades = p * u + up - gt

# resultado utilidades
print(f'utilidades del proyecto: {utilidades}')