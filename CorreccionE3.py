def calcular_iva(subtotal):
    return subtotal * 0.15

def procesar_venta(subtotal):
    iva = calcular_iva(subtotal)
    return subtotal + iva

iva_aplicado = calcular_iva(2000)
total = procesar_venta(2000)

print("IVA calculado directamente: C$", iva_aplicado)
print("Total de la venta: C$", total)