#Funciones
def sumar(x,y):
  return x + y
def restar(x,y):
  return x - y
def mutiplicar(x,y):
  return x * y
def dividir(x,y):
  if y!= 0:
    return x/y
  else:
    return 'Error Matematico'
def potencia(x,y):
  return x**y
def raiz_cuadrada(x):
  if x > 0:
    return x ** 0.5
  else:
    return 'Error Matematico'
  
#Menu Contextual

def calculadora():
  print("¡Bienvenido a la Calculadora!")
  while True: 
    eleccion = int(input("Selecciona una operación (Sumar (1) /Restar (2)/Multiplicar (3) /Dividir (4) /Potencia (5) /Raiz Cuadrada (6)): "))
    if eleccion == 7:
      break
    
    elif eleccion in [1,2,3,4,5,6]:
      x = int(input('introduce el primero numero: '))
      y = int(input('introduce el segundo numero: '))
      if eleccion ==1:
        result = sumar(x,y)
      if eleccion ==2:
        result = restar(x,y)
      if eleccion ==3:
        result = mutiplicar(x,y)
      if eleccion ==4:
        result = dividir(x,y)
      if eleccion ==5: 
        result = potencia(x,y)

    elif eleccion == 6:
      x= int(input('Introduce el numero sobre el cual realizar raiz cuadrada: '))
      result = raiz_cuadrada(x)
    else:
      print(f'{eleccion} no es una opcion valida')

  
    print(result)

#Main formula 
if __name__ == "__main__": 
  calculadora()