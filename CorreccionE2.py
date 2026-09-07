def registrar_venta(total_actual):
    print("Venta registrada")
    return total_actual + 1

ventas_registradas = 0
ventas_registradas = registrar_venta(ventas_registradas)
ventas_registradas = registrar_venta(ventas_registradas)

print("Total de ventas:", ventas_registradas)