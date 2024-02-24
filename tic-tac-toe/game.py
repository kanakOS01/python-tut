import time
from player import HumanPlayer, ComputerPlayer, AIComputerPlayer

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] -> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves    
        # list comprehension

        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter

            # check for winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
    
        # diagnols
        # positions - [0, 2, 4, 6, 8]
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag2]):
                return True
            
        return False


def play(game, x_player, o_player, print_game=True):
    # returns None in the case of tie
    if print_game:
        game.print_board_nums()

    letter = 'x' # starting letter
    while game.empty_squares():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(letter + ' wins')
                return letter

            letter = 'o' if letter == 'x' else 'x'
        
        if print_game:
            time.sleep(1)
        
    if print_game:
        print("It's a tie")
             

if __name__ == "__main__":
    # x_player = HumanPlayer('x')
    ai_wins = 0
    comp_wins = 0
    ties = 0

    for _ in range(1000):
        o_player = ComputerPlayer('o')
        x_player = AIComputerPlayer('x')
        t = TicTacToe()
        res = play(t, x_player, o_player, False)
        if res == 'x':
            ai_wins += 1
        elif res == 'o':
            comp_wins += 1
        else:
            ties += 1

    print(ai_wins)
    print(comp_wins)
    print(ties)