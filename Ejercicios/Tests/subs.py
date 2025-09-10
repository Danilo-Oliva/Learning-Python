correos_anteriores = set()
correos_nuevos = set()

def ingresar_correos(mensaje):
  lista = input(mensaje).split(",")
  return set(c.strip().lower() for c in lista if c.strip())

while True:
  print("\n--- GESTOR DE LISTAS DE CORREO ---")
  print("1 - Ingresar lista anterior")
  print("2 - Ingresar lista nueva")
  print("3 - Mostrar comparación")
  print("0 - Salir")

  opcion = int(input("Opción: "))
  
  match opcion:
    case 1:
      correos_anteriores = ingresar_correos("Ingrese correos anteriores seguido por una coma: ")
    case 2:
      correos_nuevos = ingresar_correos("Ingrese correos nuevos ")
    case 3:
      if not correos_anteriores or not correos_nuevos:
        print("Primero debe ingresar ambas listas")
      else:
        print("Mostrando suscriptores")
        print("suscriptores que siguen: ", correos_nuevos & correos_anteriores)
        print("Suscritores nuevos: ", correos_nuevos - correos_anteriores)
        print("Suscritores que se fueron: ",correos_anteriores - correos_nuevos)
        print("Suscritores totales: ", correos_anteriores | correos_nuevos)
    case 0:
      break
    case _:
      print("Opcion invalida")
      