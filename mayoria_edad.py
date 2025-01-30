edad = int(input("Ingrese su edad: "))
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Te redirijo a google")

print("Flujo con funcion")

#Con funciones

def verificar_edad(edad):
    if edad>=18:
        print("Eres mayor de edad")
    else:
        print("Te redirijo a google")

edad_usuario=int(input("Ingrese su edad: "))
verificar_edad(edad_usuario)