
productos_disponibles = 100

def vender_producto(cantidad):

    global productos_disponibles
    
    if cantidad <= 0:
        print(" Error: La cantidad a vender debe ser mayor a 0.")
    elif cantidad > productos_disponibles:
        print(f" Error: Stock insuficiente. Solo hay {productos_disponibles} productos disponibles.")
    else:
        productos_disponibles -= cantidad
        print(f"Venta exitosa: Se vendieron {cantidad} producto(s).")

def reabastecer(cantidad):
    global productos_disponibles
    
    if cantidad <= 0:
        print(" Error: La cantidad a reabastecer debe ser mayor a 0.")
    else:
        productos_disponibles += cantidad
        print(f" Reabastecimiento exitoso: Ingresaron {cantidad} producto(s) al inventario.")

def consultar_inventario():

    print(f"Inventario actual: {productos_disponibles} productos disponibles.")
    return productos_disponibles

def inventario_bajo():
    return productos_disponibles < 10

def reporte_inventario():
    print("\n" + "="*30)
    print("REPORTE DE INVENTARIO")
    print("="*30)
    print(f"Productos en stock: {productos_disponibles}")
    
    if inventario_bajo():
        print("Estado general:  ALERTA - Inventario bajo.")
    else:
        print("Estado general:  Óptimo - Stock suficiente.")
    print("="*30 + "\n")

if __name__ == "__main__":

    reporte_inventario()
    
    vender_producto(20)
    consultar_inventario()
    
    vender_producto(90)
    
    vender_producto(75)
    reporte_inventario() 
    
    reabastecer(50)
    reporte_inventario()