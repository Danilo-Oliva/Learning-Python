vec_num = []

for _ in range(10):
  numeros = int (input("Ingrese numero: "))
  vec_num.append(numeros)
  
positivos = [n for n in vec_num if n > 0]
negativos = [n for n in vec_num if n < 0]

if negativos:
  max_neg = max(negativos)
  print(f'El maximo de los negativos es: {max_neg}')
else:
  print("No se han ingresado numeros negativos")
if positivos:
  max_pos = max(positivos)
  print(f'El maximo de los positivos es: {max_pos}')
else:
  print("No se han ingresado numeros positivos")
