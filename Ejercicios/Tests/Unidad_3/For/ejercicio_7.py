vector = []
positivos = 0
negativos = 0
ceros = 0

print("Ingrese 10 numeros a continuacion")
for i in range(10):
  numeros = int(input("Ingrese numeros: "))
  vector.append(numeros)

for numeros in vector:
  if numeros > 0:
    positivos += 1
  elif numeros < 0:
    negativos += 1
  else:
    ceros += 1

print(f'Cantidad de numeros: positivos: {positivos}, negativos: {negativos} e iguales a cero: {ceros}')