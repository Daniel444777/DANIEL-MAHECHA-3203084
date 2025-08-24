edad = 20
tiene_cedula = True

if edad >= 18 and tiene_cedula:
    print("Puedes entrar a la discoteca")
else:
    print("No puedes entrar")

# Uso de or
if edad < 18 or not tiene_cedula:
    print("No cumples los requisitos")
