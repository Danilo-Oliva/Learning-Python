marca_a = int (input ("Ingrese la cantidad de alfajores vendidos por la marca A: "))
marca_b = int (input ("Ingrese la cantidad de alfajores vendidos por la marca B: "))
marca_c = int (input ("Ingrese la cantidad de alfajores vendidos por la marca C: "))

total_vendido = marca_a + marca_b + marca_c

porcentaje_a = marca_a * 100 / total_vendido
porcentaje_b = marca_b * 100 / total_vendido
porcentaje_c = marca_c * 100 / total_vendido

print (f'El porcentaje vendido por la marca A fue de:{porcentaje_a}')
print (f'El porcentaje vedido por la marca B fue de: {porcentaje_b}')
print (f'El porcentaje vendido por la marca C fue de: {porcentaje_c}')