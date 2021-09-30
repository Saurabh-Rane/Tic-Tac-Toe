#Tic tac toe game

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

player = "X"
game_status = True
winner = None

def play_game():
  display_board()
  while game_status:
    # play a single turn
    play_turn(player)
    check_result()
    flip_chance()

  return None

def display_board():
  print(board[0] + " " + board[1] + " " + board[2] + "\t\t 1 | 2 | 3 ")
  print(board[3] + " " + board[4] + " " + board[5] + "\t\t 4 | 5 | 6 ")
  print(board[6] + " " + board[7] + " " + board[8] + "\t\t 7 | 8 | 9 ")
  return None

def play_turn(p):
  global player
  print(p + "'s turn")
  position = input("Enter the position from 1-9 : ")
  flag = "Invalid"
  while flag == "Invalid":
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] :
      position = input("Enter the position from 1-9 : ")
    position = int(position) - 1
    if board[position] == "-":
      flag = "Valid"
    else :
      print("Position already filled, enter new position from 1-9")
  board[position] = p
  display_board()
  return None

def flip_chance():
  global player
  if player == "X":
    player = "O"
  elif player == "O":
    player = "X"
  return None

def check_result():
  global winner
  check_win()
  check_tie()
  if winner == "X":
    print("X won")
  elif winner == "O":
    print("O won")
  elif winner == "Tie":
    print("Tie")
  return None

def check_win():
  global game_status
  if check_row():
    game_status = False
  if check_column():
    game_status = False
  if check_diagonal():
    game_status = False
  return None

def check_row() :
  global winner
  if board[0] == board [1] == board[2] != "-":
    winner = board[0]
    return True
  elif board[3] == board [4] == board[5] != "-":
    winner = board[3]
    return True
  elif board[6] == board [7] == board[8] != "-":
    winner = board[6]
    return True
  else:
    return False

def check_column():
  global winner
  if board[0] == board [3] == board[6] != "-":
    winner = board[0]
    return True
  elif board[1] == board [4] == board[7] != "-":
    winner = board[1]
    return True
  elif board[2] == board [5] == board[8] != "-":
    winner = board[2]
    return True
  else:
    return False

def check_diagonal() :
  global winner
  if board[0] == board [4] == board[8] != "-":
    winner = board[0]
    return True
  elif board[6] == board [4] == board[2] != "-":
    winner = board[1]
    return True
  else:
    return False

def check_tie():
  global game_status
  global winner
  if "-" not in board:
    winner = "Tie"
    game_status = False
    

  

play_game()