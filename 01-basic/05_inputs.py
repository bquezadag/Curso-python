nombre = input("Hola como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("Cuantos años tienes?\n")
age = int(age)

print(f"Dentro de 20 años tendras {age + 20}")


print("obtener multiples valores a la vez")

country, city = input("¿en que pais y ciudad vives?\n").split()
print(f"Vives en {country}, {city}")
