import numpy as np

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.board = np.array(self.board)
    def show_board(self):
        print("-" * 2 * self.size)
        print(self.board)
        print("-" * 2 * self.size)
    def change_value(self, x, y, value):
        if ((0 <= x - 1 < self.size) and (0 <= y - 1 < self.size) \
            and (value in [-1, 0, 1])):
            self.board[x - 1][y - 1] = value
            return (1)
        else:
            print("Invalid position")
            return (0)
    def check_game_over(self):
        return (0)

#Idea: write instructions aobut how to play
my_go_match = Board(4)
my_go_match.show_board()

#Game starts
#Player with white stones = 1
#Player with black stones = 0
player = -1
while(not my_go_match.check_game_over()):
    if(player == -1):
        player = 1
        print("Is player with white stones turn")
    else:
        player = -1
        print("Is player with black stones turn")
    x, y = map(int, input("Make your move by introducing a position: ").split())
    my_go_match.change_value(x, y, player)
    my_go_match.show_board()