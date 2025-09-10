minutos_ingresados = int (input ("Ingrese una cantidad de minutos: "))

dias = minutos_ingresados // 1440
minutos_restantes = minutos_ingresados % 1440
horas = minutos_restantes // 60
minutos = minutos_restantes % 60 

print (f'Los minutos ingresados equivale a: {dias} dias, {horas} horas y {minutos} minutos')