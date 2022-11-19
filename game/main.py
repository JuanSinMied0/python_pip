#Juego: Piedra, papel o tijera
import random
def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("Piedra, papel o tijera => ")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("OPCION INGRESADA NO ES VALIDA")
    #continue
    return None, None

  computer_option = random.choice(options)
  print("Eleccion usuario =>", user_option)
  print("Eleccion computadora =>", computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  
  if user_option == computer_option:
    print("¡EMPATE!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("¡Piedra gana a tijera, ¡USUARIO GANA!")
      user_wins += 1
    else:
      print("Papel gana a piedra, ¡COMPUTADORA GANA!")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Papel gana a piedra, ¡USUARIO GANA!")
      user_wins += 1
    else:
      print("Tijera gana a papel, ¡COMPUTADORA GANA!")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera gana a papel, USUARIO GANA!")
      user_wins += 1
    else:
      print("Piedra gana a tijera, COMPUTADORA GANA!")
      computer_wins += 1
  return user_wins, computer_wins
def check_wins(user_wins, computer_wins):
  if computer_wins == 2:
    print("EL GANADOR DEL JUEGO ES LA COMPUTADORA")
    exit()
  elif user_wins == 2:
    print("EL GANADOR DEL JUEGO ES EL USUARIO")
    exit()
  return 
def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1
  while True:
    print("*" * 15)
    print("RONDA", rounds)
    print("*" * 15)
    print("VICTORIAS DE LA COMPUTADORA", computer_wins)
    print("VICTORIAS DEL USUARIO", user_wins)
    rounds += 1
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    check_wins(user_wins, computer_wins)
run_game()