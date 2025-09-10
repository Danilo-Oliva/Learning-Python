import math

def calcularRaiz():
  base = float(input("Ingrese la base: "))
  indice = float(input("Ingrese el indice: "))
  resultado = base ** (1 / indice)
  print(f"\nLa raiz {indice} de base {base} es: {resultado}")
  
def calcularPotencia():
  base = float(input("Ingrese la base: "))
  exponente = float(input("Ingrese el exponente: "))
  resultado = math.pow(base, exponente)
  print(f"\nEl numero {base} elevado a {exponente} es: {resultado}")

while True:
  print("\nBIENVENIDO A LA CALCULADORA DE POTENCIA")
  print("1 - Calcular Raiz")
  print("2 - Calcular Potencia")
  print("0 - Salir")
  opcion = int(input("Opcion: "))
  
  if opcion == 0:
    break
  
  match opcion:
    case 1:
      calcularRaiz()
    case 2:
      calcularPotencia()
    case _:
      print("Opción invalida")