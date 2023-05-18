horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))

if horas_trabajadas <= 4:
    importe_pagar = 6
else:
    importe_pagar = 6 + (horas_trabajadas - 4) * 2

print("El importe a pagar es:", importe_pagar, "soles.")