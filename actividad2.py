#Nivel Facil
print("Nivel Facil!")

nombre = "Benjamin"
edad = 20
estatura = "1.70"
print(nombre, edad, estatura)

añonacimiento = 2004
añoactual = 2025
edad = añoactual - añonacimiento
print("La edad es:", edad)

#Nivel Medio
print("Nivel Medio!")

precio = 10000
descuento = 0.15
precio_final = precio - (precio * descuento)
print("El precio final es:", precio_final)

edad = 20
edad_meses = edad * 12
edad_semanas = edad * 52
edad_dias = edad * 365
edad_horas = edad_dias * 24

print("Edad en meses:", edad_meses)
print("Edad en semanas:", edad_semanas)
print("Edad en días:", edad_dias)
print("Edad en horas:", edad_horas)

#Nivel Dificil
print("Nivel Dificil!")

nota1 = 7.0
nota2 = 7.0
nota3 = 7.0
promedio = (nota1 + nota2 + nota3) / 3
print("El promedio es:", promedio)
if promedio >= 7:
    print("Aprobado")
