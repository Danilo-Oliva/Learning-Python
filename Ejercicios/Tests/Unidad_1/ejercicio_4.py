cantidad_asientos_totales = int ( input("Ingrese la cantidad de asientos: ") )
cantidad_asientos_ocupados = int ( input("Ingrese la cantidad de asientos ocupados: ") )

porcentaje_ocupacion = (cantidad_asientos_ocupados * 100)/cantidad_asientos_totales
porcentaje_desocupacion = 100 - porcentaje_ocupacion

print (f'El porcentaje de ocupacion es del: {porcentaje_ocupacion} ')
print (f'El porcentaje de desocupacion es del: {porcentaje_desocupacion}' )