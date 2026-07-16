c0 = int(input("Ingresa un número entero positivo: "))

# Inicializamos el contador de pasos en 0
steps = 0

# 2. El bucle se ejecuta mientras c0 sea diferente de 1
while c0 != 1:
    # Si el número es par (el residuo de dividir entre 2 es cero)
    if c0 % 2 == 0:
        c0 = c0 // 2  # Usamos // para mantenerlo como entero
    # Si el número es impar
    else:
        c0 = 3 * c0 + 1
    
    # Imprimimos el valor intermedio actual
    print(c0)
    
    # Sumamos un paso al contador
    steps += 1

# 3. Al salir del bucle (cuando c0 ya es 1), imprimimos el total de pasos
print("steps =", steps)
