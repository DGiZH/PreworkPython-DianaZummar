
def crear_tablero():
  tablero = [[" " for iterador in range (3)] for iterador in range(3)]
  return tablero

def imprimir_tablero():
  tablero = crear_tablero()
  print("-" * 9)
  for fila in tablero:
    print(" | ".join(fila))
    print("-" * 9)

def is_tablero_lleno(tablero):
  return all(all(casilla != " " for casilla in fila) for fila in tablero)

def comprobar_ganador(tablero, jugador):
  for i in range(3):
    for j in range(3):
      if all(tablero [i][j] == jugador) or all(tablero [j][i] ==jugador):
        return True
      
      if all(tablero [i][i] == jugador) or all(tablero [j][2-i] ==jugador):
        return True
  return False


# control de flujo

def tres_en_linea():
  tablero = crear_tablero()
  jugador_actual = 'X'

  print('Bienvenido/a! Estais jugando al tres en línea')
  imprimir_tablero(tablero)
  while True:
    
    print(f"Turno de Jugador: {jugador_actual}")
    fila = int(input('Elige Fila 0, 2, 2: '))
    columna = int(input('Elige Fila 0, 2, 2: '))
    if tablero[fila][columna] != " ":
      tablero[fila][columna] = jugador_actual
      if comprobar_ganador(tablero, jugador_actual):
        print(f'El jugador {jugador_actual} ha ganado!')
        break
      if is_tablero_lleno(tablero):
        print('Empate!!')
        break
      
      jugador_actual = 'O' if jugador_actual == 'X' else 'X'
      #if jugador_actual == 'X'
      #   jugador_actual = 'O'
      # else:
      #   jugador_actual = 'O' 
    
    else:
      print('Casilla ocupada')

  
if _name_ == '_main_':
  tres_en_linea()
