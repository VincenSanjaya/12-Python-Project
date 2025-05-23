import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter
    
    # we want all players to get their next move fiven a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    
    def get_move(self, game):
        # get random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # we're going to check is a correct value by trying to cast
            # it to an int, and if its not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')
        
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        
        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # maximize the max_player
        else:
            best = {'position': None, 'score': math.inf} # minimize the other player
        
        for possible_move in state.available_moves():
            # step 1: try a spot on the board
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # now we alternate players
            
            # step 3: undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # step 4: update the best move
            if player == max_player: # maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else: # minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best