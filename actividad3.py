#Operadores

# Operadores aritméticos básicos
a = 10
b = 3
suma = a + b # 13
resta = a - b # 7
multiplicacion = a * b # 30
division = a / b # 3.3333... (resultado decimal)
division_entera = a // b # 3 (división sin decimales)
modulo = a % b # 1 (resto de la división)
potencia = a ** b # 1000 (10 elevado a 3)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Potencia:", potencia)

# Operadores de comparación
x = 7
y = 10
igual = x == y # False (¿x es igual a y?)
diferente = x != y # True (¿x es diferente de y?)
mayor = x > y # False (¿x es mayor que y?)
menor = x < y # True (¿x es menor que y?)
mayor_igual = x >= y # False (¿x es mayor o igual que y?)
menor_igual = x <= y # True (¿x es menor o igual que y?)
print("¿Iguales?", igual)
print("¿Diferentes?", diferente)
print("¿Mayor?", mayor)
print("¿Menor?", menor)
print("¿Mayor o igual?", mayor_igual)
print("¿Menor o igual?", menor_igual)

# Operadores lógicos
tiene_entrada = True
es_vip = False
# Operador AND (y)
puede_entrar_vip = tiene_entrada and es_vip # False
print("¿Puede entrar al área VIP?", puede_entrar_vip)
# Operador OR (o)
puede_entrar_evento = tiene_entrada or es_vip # True
print("¿Puede entrar al evento?", puede_entrar_evento)
# Operador NOT (no)
no_es_vip = not es_vip # True
print("¿No es VIP?", no_es_vip)
# Combinando operadores
edad = 16
con_adulto = True
puede_ver_pelicula = edad >= 18 or (edad >= 13 and con_adulto)
print("¿Puede ver la película?", puede_ver_pelicula)

print("Actividad 3")
print("Nivel Fácil!")

base = 5
altura = 3
area = base * altura # Área = base * altura
perimetro = 2 * (base + altura) # Perímetro = 2 * (base + altura)
print("Área del rectángulo:", area)
print("Perímetro del rectángulo:", perimetro)

# Comparación de 15 elevado a 2 con 200
es_mayor = (15 ** 2) > 200
print("¿15^2 es mayor que 200?", es_mayor)