vec_nums_ings = []
for i in range(2):
  numeros = int(input("Ingrese 2 numeros: "))
  vec_nums_ings.append(numeros)
  
  mayor = max(vec_nums_ings)
  menor = min(vec_nums_ings)
  
for x in range(menor + 1, mayor):
  print(x)