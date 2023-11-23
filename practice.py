def mcd(a, b):
  while b: a, b = b, a % b 
  return a 
num1 = int(input("Ingresa el primer número: ")) 
num2 = int(input("Ingresa el segundo número: ")) 
print("El MCD es:", mcd(num1, num2))

