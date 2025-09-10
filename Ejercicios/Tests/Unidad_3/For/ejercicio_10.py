vector = []

for _ in range(10):
  numeros = int(input("Ingrese numero: "))
  vector.append(numeros)

maximo = max(vector)
posicion = vector.index(maximo) +1 #+1 para que se entienda en que posicion fue ingresado, no la posicion del vector

print(f'El maximo de la lista es: {maximo} y su posicion es: {posicion}')