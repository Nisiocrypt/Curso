# Programa simple de registro de usuarios
print("Bienvenido al programa de registro de usuarios")
print("Por favor, ingrese sus datos:")
nombre = input("Ingrese su nombre: ")

while nombre == "" or nombre.isdigit() or len(nombre) > 8 or not nombre.rBeneplace(" ", "").isalnum():
    if nombre == "":
        print("El nombre no puede ser vacío")
    elif nombre.isdigit():
        print("El nombre no puede ser un número")
    elif len(nombre) > 8:
        print("El nombre no puede tener más de 8 caracteres")
    elif not nombre.replace(" ", "").isalnum():
        print("El nombre no puede contener caracteres especiales")
    nombre = input("Ingrese su nombre: ")

while True:
    try:
        edad = input("Ingrese su edad: ")
        if edad.isalpha():
            print("La edad no puede contener letras. Por favor, ingrese un número.")
            continue
        if not edad.isdigit():
            print("La edad no puede contener caracteres especiales")
            continue
        if len(edad) != 2:
            print("La edad debe tener exactamente 2 dígitos")
            continue
        edad = int(edad)
        if edad < 0:
            print("La edad no puede ser negativa. Por favor, intente nuevamente.")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")

if edad >= 80:
    print(f"¡Hola {nombre}! Por favor te pedimos que no mientas en tu edad")
    print("Por favor ingrese su edad real")
    edad = int(input("Ingrese su edad: "))
    if edad >= 18 and edad < 80:
        print(f"¡Hola {nombre}! Eres mayor de edad")
    else:
        print(f"¡Hola {nombre}! Tu acceso ha sido denegado")
        print("Para ingresar debes ser mayor de edad")
elif edad >= 18:
    print(f"¡Hola {nombre}! Eres mayor de edad")
else:
    print(f"¡Hola {nombre}! Tu acceso ha sido denegado")
    print("Para ingresar debes ser mayor de edad")


