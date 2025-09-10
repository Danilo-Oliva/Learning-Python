def esPrimo(numero):
  if numero < 2:
    return False
  else:
    for i in range(2,int(numero**0.5) + 1):
      if numero % i == 0:
        return False
    return True

numero = int(input("Ingrese numero: "))
if esPrimo(numero):
  print("Es primo")
else:
  print("No es primo")    


