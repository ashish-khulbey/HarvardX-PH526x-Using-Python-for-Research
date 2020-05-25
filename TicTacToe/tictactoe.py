import numpy as np
import random

def create_board():
  return np.zeros((3,3), dtype=int)

def place(board, player, position):
  x,y=position
  if board[x][y]==0:
    board[x][y]=player

def possibilities(board):
  index = list(zip(*np.where(board==0)))
  return index

def random_place(board, player):
  index = possibilities(board)
  position = random.choice(index)
  place(board, player, position)

def row_win(board, player):
    if np.any(np.all(board==player, axis=1)): # this checks if any column contains all positions equal to player
        return True
    else:
        return False

def col_win(board, player):
    if np.any(np.all(board==player, axis=0)): # this checks if any column contains all positions equal to player
        return True
    else:
        return False

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

random.seed(1)

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

def play_strategic_game():
  board = create_board()
  board[1][1] = 1
  winner = 0
  while winner == 0:
    for player in [2, 1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
  return winner     

results = [play_strategic_game() for i in range(1000)]
print(results.count(1))


# board = create_board()
# # place(board, 1, (0,0))
# # random_place(board, 2)
# player = 1 
# for i in range(6):
#   random_place(board, player)
#   # print(board)
#   if player==1:
#     player = 2
#   elif player==2:
#     player = 1 

# # print(row_win(board, 1))
# # print(col_win(board, 1))
# board[1,1] = 2
# # print(diag_win(board, 2))
# print(evaluate(board))
# print(board)
