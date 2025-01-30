productos=[]
precios=[]
for i in range(3):
    nombre=input("Ingrese el nombre del producto: ")
    precio=float(input(f"Ingrese el precio del producto {nombre}"))
    productos.append(nombre)
    precios.append(precio)
total=0
for precio in precios:
    total+=precio
if total>100:
    total=total*0.90
print("Resumen de compra: ")
for i in range(len(productos)):
    print(f"{productos[i]} - ${precios[i]:.2f}")

print(f"total a pagar: ${total:.2f}")


def registrar_productos():
    productos=[]
    precios=[]  
    for i in range(3):
        nombre=input("Ingrese el nombre del producto: ")
        precio=float(input(f"Ingrese el precio del producto {nombre}"))
        productos.append(nombre)
        precios.append(precio)
    return productos,precios

