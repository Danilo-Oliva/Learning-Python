positivos = 0
tam = int(input("Ingrese cantidad de numeros que va a ingresar: "))
vector = []

for i in range(tam):
  numeros = int(input("Ingrese los numeros: "))
  vector.append(numeros)

for numeros in vector:
  if numeros > 0:
    positivos += 1

print(f'la cantidad de numeros positivos son: {positivos}')
