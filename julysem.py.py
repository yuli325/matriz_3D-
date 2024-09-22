def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return f"Monto Total: ${monto_total:.2f}, Descuento: ${descuento:.2f}, Monto Final: ${monto_final:.2f}"

# Primera llamada: solo con monto total (usa el porcentaje por defecto)
print("Primera llamada:")
print(calcular_descuento(1000))
print()

# Segunda llamada: con monto total y porcentaje de descuento
print("Segunda llamada:")
print(calcular_descuento(10000, 15))
