import math
import random

class Player: 
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        moves = game.available_moves()
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0 - 8):")
            try:
                val = int(square)
                if val not in moves:
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")

        return val

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        return random.choice(game.available_moves())

class AIComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get square using minimax algo
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'o' if self.letter == 'x' else 'x'
        
        # check if previous move is winner or not
        # this is the base case
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}   # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}   # each score should minimize
    
        for possible_move in state.available_moves():
            # 1. make a move and try that spot
            # 2. recursively call minimax with the new state
            # 3. undo the move you make
            # 4. update the dictionary

            state.make_move(possible_move, player)
            temp_score = self.minimax(state, other_player)

            # undoing
            state.board[possible_move] = ' '
            state.current_winner = None

            temp_score['position'] = possible_move

            if player == max_player:
                if temp_score['score'] > best['score']:
                    best = temp_score
            else:
                if temp_score['score'] < best['score']:
                    best = temp_score
            
        return best
    