#Entrada
importe = int (input ('Ingrese el importe a pagar: $'))
descuento = int (input ('Ingrese el descuento: %'))

#proceso
calcular_descuento = (100 - descuento) / 100
precio_final = importe * calcular_descuento

#salida
print (f'El precio final es de: ${precio_final}')