#Variables y Operadores

#1. Ejercicio: Crea una variable llamada nombre y asígnale tu nombre como valor. Luego imprime la variable
nombre = 'Diana'
print(nombre)

#2. Ejercicio : Crea dos variables, a y b , y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de a y b .
a = 5
b = 10
print(a+b)

#3. Ejercicio Ejercicio: Calcula el área de un triángulo con base 10 y altura 5
area_triangle = a * b / 2
print(area_triangle)

#4. Ejercicio: Calcula el resto de dividir 17 entre 3.
print(17%3)

# Condicionales

#1. Ejercicio: Dado un número, imprime si es positivo o negativo.
numero = 4
if numero <0 :
  print( 'negativo')
else:
  print('positivo')

#2. Ejercicio: Dado un número, imprime si es par o impar.
x = 5
if x%2 ==0:
    print('The number is even')
else:
    print('The number is odd')

#3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
a = 3
b = 40
c = 9

if a>b and a>c :
  print(a)
if b>a and b>c :
  print(b)
if c>a and c>b :
  print(c)
    
# Bucles
#1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
  print(numero)

#2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while

i = 1
while i <=20 :
  if i%2==0:
    print(i)
  i +=1

#3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
n=1
suma=0
while n<=100:
  suma += n
  n +=1
print(suma)

#Funciones
#1. Ejercicio: Define una función que tome dos números y retorne su suma.
def sumar(a,b):
  print(f'la suma total es de {a+b}')

#2. Ejercicio: Define una función que tome un número y retorne su factorial.
def factorial(n):
  if n==0 or n==1:
    resultado = 1
    print(resultado)
  elif n>1:
    resultado= n * factorial(n-1)
    print(resultado)
  return resultado

#3. Ejercicio: Define una función que tome un número y determine si es primo.
def prime(n):
  if n%2 == 0:
    print('este numero es primo')
  elif n%2 >0:
    print('este numero es compuesto')
  return

prime(3)

#4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
def suma_numeros(list):
  sum(list)
  result = sum(list)
  return print(f'el resultado de la suma es {result}')
list = [1,3,3]
suma_numeros(list)

#5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
def reverse(a):
  text_reverse= a [::-1]
  print(text_reverse)
  return 

#Bucles y Funciones

#1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
def es_par(numero):
  numero = int(input("Ingresa un número: "))
  if numero%2 == 0:
    print("El número es par")
  else:
    print("El número es impar")
    
es_par(1)

#1. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
def factorial(numero):
  resultado = 1
  for i in range(1, numero+1):
    resultado *= i
  return resultado
num = int(input("Ingresa un número: "))
print(f"El factorial de {num} es: {factorial(num)}")

#1. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.

def contar_digitos(numero):
  return len(str(numero))
num = int(input('Ingresa un número:'))
print('la cantidad de digitos es:',contar_digitos(num))

#1. Dada una lista de números, crea una función que devuelva el número máximo de la lista
def encontrar_maximo(lista):
  maximo = lista[0] 
  for numero in lista: 
    if numero > maximo: 
      maximo = numero 
  return maximo 
numeros = [5,12,25,98,9] 
print("El número máximo es:", encontrar_maximo(numeros))

#1. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
def sumar_digitos(numero): 
  suma = 0 
  while numero > 0: 
    suma += numero % 10 
    numero //= 10
  return suma
   
num = float(input("Ingresa un número: ")) 
print("La suma de los dígitos es:", sumar_digitos(num))

#1. Dados dos números, crea una función para encontrar el mínimo común múltiplo(MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.

def mcm(a, b):
  if a == 0 or b == 0: 
    return 0 
  else: 
    maximo = max(a, b) 
    while True: 
      if maximo % a == 0 and maximo % b == 0: 
        return maximo 
      maximo += 1 
num1 = int(input("Ingrese el primer número: ")) 
num2 = int(input("Ingrese el segundo número: ")) 
print("El MCM es:", mcm(num1, num2))

#1. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
b = int(input('Ingrese la base del triangulo: '))
a = int(input ('Ingrese la altura del traingulo: '))

def traingle(a,b):
  return (a + b) / 2
print('El area del triangulo es:',traingle(a,b))
traingle(a,b)

#1. Crea una función que, dado un número, verifique si un número es positivo,negativo o cero
def verificar_signo(n):
  if n==0:
    return'cero'
  elif n<0:
    return 'negativo'
  else: 
    return 'positivo'

n = int(input('Ingrese un numero:' ))
print ('El numero es:', verificar_signo(n))

#1. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
def contar_letras(palabra):
  contador = 0
  for letra in palabra:
    if letra.isalpha():
      contador += 1
  return contador
palabra = input('Ingrese una palabra: ')
print(f'la cantidad de letras en {palabra} son ',contar_letras(palabra))

#1. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.

def valor_abs(lista):
  for i in range(len(lista)):
    lista[i]= abs(lista[i])
  return lista 

lista = [1, -3, -4,20 ,-3,4]
print('El valor absoluto de la lista es:',valor_abs(lista))

#1. Crea una función que, dado un número, verifique si un número es primo.
def es_primo(numero): 
  if numero <= 1: 
    return False 
  for i in range(2, numero):
    if numero % i == 0: 
      return False 
  return True 
num = int(input("Ingresa un número: ")) 
if es_primo(num):
  print("Es un número primo.")
else: print("No es un número primo.")

#1. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.
def mcd(a, b):
  while b: a, b = b, a % b 
  return a 
num1 = int(input("Ingresa el primer número: ")) 
num2 = int(input("Ingresa el segundo número: ")) 
print("El MCD es:", mcd(num1, num2))
  
  
  


  



