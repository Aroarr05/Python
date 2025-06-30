import re

email = input("Ingresa un correo electrónico: ")
patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(patron, email):
    print("Correo válido.")
else:
    print("Correo inválido.")