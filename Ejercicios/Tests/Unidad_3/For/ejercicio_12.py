vec_num = []
pares = 0
for _ in range(10):
  numeros = int(input("Ingrese numero: "))
  vec_num.append(numeros)
  if numeros % 2 == 0:
    pares += 1

vec_pares = [n for n in vec_num if n % 2 == 0]
max_par = max(vec_pares)

print (f'La cantidad de pares es de: {pares} y el maximo par ingresado es: {max_par}')



