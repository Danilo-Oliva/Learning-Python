vec_num = []
positivos = 0
negativos = 0
ceros     = 0
total     = 0

print("A continuacion ingrese 10 numeros")
for _ in range(10):
  numeros = int(input("Ingrese numero: "))
  total += 1
  vec_num.append(numeros)

for numeros in vec_num:
  if numeros > 0:
    positivos += 1
  elif  numeros < 0:
    negativos += 1
  else:
    ceros += 1

porcentaje_positivos = positivos * 100 / total
porcentaje_negativos = negativos * 100 / total
porcentaje_ceros = ceros * 100 / total

print(f'El porcentaje de positivos es de: {porcentaje_positivos}, de negativos es: {porcentaje_negativos} y de ceros es de: {porcentaje_ceros}')