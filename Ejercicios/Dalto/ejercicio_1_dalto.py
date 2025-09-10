curso_actual = 1.5
curso_minimo = 2.5
curso_promedio = 4
curso_maximo = 7

resultado_a_1 = 100 - curso_actual / curso_minimo * 100 
resultado_a_2 = 100 - curso_actual * 1000 // curso_maximo / 10
resultado_a_3 = 100 - curso_actual / curso_promedio * 100 

#A
print("Pregunta A")
print(f'El curso actual dura un: {resultado_a_1}% menos que el más rapido')
print(f'El curso actual dura un: {resultado_a_2}% menos que el más lento')
print(f'El curso actual dura un: {resultado_a_3}% menos que el promedio')