primer_semana = int (input ("Ingrese recaudacion de la primera semana: $"))
segunda_semana = int (input("Ingrese recaudacion de la segunda semana: $") )
tercera_semana = int (input ("Ingrese recaudacion de la cuarta semana: $"))
cuarta_semana = int (input ("Ingrese recaudacion de la cuarta semana: $"))

#total
total = primer_semana + segunda_semana + tercera_semana + cuarta_semana

#promedio
promedio = total / 4

#porcentaje
porcentaje_1 = primer_semana * 100 / total
porcentaje_2 = segunda_semana * 100 / total
porcentaje_3 = tercera_semana *100 / total
porcentaje_4 = cuarta_semana * 100 / total

#salida
print (f'La recaudacion promedio fue de: ${promedio}')
print (f'El porcentaje total de la primera semana fue de: ${porcentaje_1}')
print (f'El porcentaje total de la segunda semana fue de: ${porcentaje_2}')
print (f'El porcentaje total de la tercera semana fue de: ${porcentaje_3}')
print (f'El porcentaje total de la cuarta semana fue de: ${porcentaje_4}')