contraseña = input("Ingresa una contraseña: ")

es_valida = (
    len(contraseña) >= 8 and
    any(c.islower() for c in contraseña) and
    any(c.isupper() for c in contraseña) and
    any(c.isdigit() for c in contraseña)
)

if es_valida:
    print("Contraseña válida.")
else:
    print("Contraseña inválida. Debe tener al menos 8 caracteres, mayúsculas, minúsculas y números.")