sueldo = float(input("Ingrese su sueldo: "))

if sueldo <= 1000:
    porcentaje_donacion = 0.05
elif sueldo <= 1500:
    porcentaje_donacion = 0.07
elif sueldo <= 2000:
    porcentaje_donacion = 0.08
elif sueldo <= 5000:
    porcentaje_donacion = 0.10
else:
    porcentaje_donacion = 0.15

monto_donacion = sueldo * porcentaje_donacion

print("Su rango de ganancia es de:", sueldo, "y su donación será de:", monto_donacion)