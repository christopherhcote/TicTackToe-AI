import math
import random

class Player():
    def __init__(self,letter):
        #letter is X or O
        self.letter = letter

    def get_move(self,game):
        pass 

class RandomComputerPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
        #while valid square != True
            square = input(self.letter + 's turn. Input move (0 - 8)')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("invalid square!, try again. ")
        return val


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    

    def get_move(self,game):
        if len(game.available_moves())==9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square            

    def minimax (self, game, player):
        max_player = self.letter #yourself
        if player =='x':
            other_player ='o'
        else:
            other_player = 'x'

        if game.current_winner == other_player:
            if other_player == max_player:
                return {'position':None, 'score':1*(game.num_empty_square() + 1)}
            else:
                return {'position':None, 'score':-1*(game.num_empty_square() + 1)}
            
        elif game.empty_squares()==False:
            return {'position':None, 'score':0}
        
        if player == max_player:
            best = {'position':None, 'score':-math.inf}
        else:
            best = {'position':None, 'score':math.inf}

        for possible_move in game.available_moves():
            game.make_move(possible_move,player)
            sim_score = self.minimax(game, other_player)

            game.board[possible_move] = ' '
            game.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] >best['score']:
                    best = sim_score
            else:
                if sim_score['score']<best['score']:
                    best = sim_score
        return best

                

