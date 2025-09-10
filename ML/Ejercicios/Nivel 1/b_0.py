def esPar(numero):
  return numero % 2 == 0

  
while True:
  numero = int(input("Ingrese un numero o ingrese 0 para salir: "))
  if numero == 0:
    break
  if esPar(numero):
    print("Es Par")
  else:
    print("Es Impar")