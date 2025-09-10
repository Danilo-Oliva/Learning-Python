importe_sin_descuento = int (input ("Ingrese el importe sin descuento: $"))
importe_con_descuento = int (input ("Ingrese el importe con descuento: $"))

diferencia = importe_con_descuento * 100 / importe_sin_descuento

descuento = 100 - diferencia

#salida
print (f'El descuento aplicado al producto es de: {descuento}%')