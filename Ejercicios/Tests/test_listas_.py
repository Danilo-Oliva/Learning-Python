vector = []

for i in range(5):
  numero = int(input(f'Ingrese un numero: '))
  vector.append(numero)

for numero in enumerate(vector):
  posicion = numero[0]
  valor = numero[1]
  print(f'Los numeros ingresados son: {valor} en la posicion: {posicion}')