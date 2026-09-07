def calcular_pago(horas, tarifa):
    pago_calculado = horas * tarifa
    print("Pago dentro de la función: C$", pago_calculado)
    return pago_calculado

pago = calcular_pago(40, 120)

print("Pago fuera de la función: C$", pago)