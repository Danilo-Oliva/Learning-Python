horas_ingresadas = int(input("Ingrese una cantidad de horas: "))

dias_equivalentes = horas_ingresadas // 24
horas_equivalentes = horas_ingresadas % 24
print(f'Dias: {dias_equivalentes} Horas: {horas_equivalentes}')