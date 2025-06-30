limite = int(input("Ingresa un número límite para la secuencia de Fibonacci: "))
a, b = 0, 1
print("Secuencia de Fibonacci:")
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b