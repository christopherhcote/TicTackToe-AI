import math
from player import HumanPlayer, RandomComputerPLayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        #we will use a single list to rep 3 x 3 board
        self.board = [" " for i in range(9)] 
        #keep track of winner
        self.current_winner = None

    #borad = [" "," "," "," "," "," "," "," "," "]
    # x = board[0:3]
    # x = [" " ," "," "]
    def print_board(self):
        #divide the board list into rows
        for i in range(3):
            start = i * 3
            end = (i +1) * 3
            row = self.board[start:end]
            formatted_row = "| " + " | ".join(row) + " |"
            print(formatted_row)
        # for row in [self.board[ i*3 : (i+1)*3 ] for i in range(3)]:
        #     print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = []

        for j in range(3):
            row = []

            for i in range(j*3,(j+1)*3):
                row.append(str(i))
            number_board.append(row)
        
        for row in number_board:
            print("| " + " | ".join(row) + " |")


    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            #[x,o,x] --> [(0,x),(1,0),(2,x)]
            if spot == " ":
                moves.append(i)
        return moves

    def empty_squares(self):
        return " " in self.board
    

    def num_empty_square(self):
        return len(self.available_moves())
    

    def winner(self, square, letter):
        #check the row
        row_indx = math.floor(square/3)
        row = self.board[row_indx*3:(row_indx+1)*3]

        if all([s == letter for s in row]):
            return True

        #check the column
        col_indx = square %3
        column = [self.board[col_indx+(3*i)] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        #check the diagonal

        if square % 2 == 0:
            diagonal = [self.board[i] for i in [0,4,8]]
            if all([s == letter for s in diagonal]):
                return True

            diagona2 = [self.board[i] for i in [2,4,6]]

            if all([s == letter for s in diagona2]):
                return True
        return False
    
    def make_move(self, square, letter):
        #we have to check if the square empty or not
        if self.board[square] == " ":
            #if it empty, add the letter to this square
            self.board[square] = letter
            if self.winner(square, letter) == True:
                self.current_winner = letter
            return True
        return False





def play(game, x_player, o_player, print_game=True):
    if print_game == True:
        game.print_board_nums()


    letter = "x"#starting letter
    while game.empty_squares():
        #get the move from the player
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #function to make a move
        if game.make_move(square, letter):
            if print_game == True:
                print(letter + ' make a move to square ' , square )
                game.print_board()
                print(" ")

        if game.current_winner: 
            if print_game:
                print(letter + " wins!!")
            return #ends the loop and exits the game

        letter = 'o' if letter == 'x' else 'x'#swtich player

    if print_game:
        print("its a tie!")





if __name__ == '__main__':
    x_player = SmartComputerPlayer('x')
    o_player = SmartComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
