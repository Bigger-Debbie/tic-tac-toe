from pathlib import Path
from random import randint
import random
import time

from board import GameBoard

class TicTacToe:
    '''Represents a game of Tic Tac Toe'''

    def __init__(self):
        '''Initilizes attributes for a game of Tic Tac Toe'''
        self.avail_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player_one = {'name': '', 'token': ''}
        self.player_two = {'name': '', 'token': ''}
        self.computer_player = None
        self.whos_turn = None
        self.moves = 0
        self.game_over = False
        self.game_board = GameBoard()

    def main_loop(self):
        '''Main game loop'''
        print(f"\n{self._draw_logo()}\n\n")
        print("\t\tWelcome to Tic Tac Toe, get three in a row to win!\n")
        print("First, I got a couple questions for ya!\n")

        while True:
            self.player_one['name'] = input("Player one, whats your name: ")\
                .lower().strip()
            self.get_opponent()
            self.get_tokens()

            print("\nAlright! Thats all I needed.")
            print("At any time press 'q' to quit. Good luck!\n")
            self.get_starting()
            
            while self.game_over == False:
                if self.whos_turn == 'player_one':
                    self.game_board.draw_board()
                    move = self.get_move('player_one')
                    self.game_board.update_board(move, self.player_one['token'])
                    self.check_status()
                    self.whos_turn = 'player_two'
                    self.avail_moves.remove(move)
                    self.moves += 1
                elif self.whos_turn == 'player_two' and self.computer_player == True:
                    self.game_board.draw_board()
                    move = random.choice(self.avail_moves)
                    print("\nComputer, whats your move...\n")
                    time.sleep(randint(1, 10))
                    self.game_board.update_board(move, self.player_two['token'])
                    self.check_status()
                    self.whos_turn = 'player_one'
                    self.avail_moves.remove(move)
                    self.moves += 1
                elif self.whos_turn == 'player_two':
                    self.game_board.draw_board()
                    move = self.get_move('player_two')
                    self.game_board.update_board(move, self.player_two['token'])
                    self.check_status()
                    self.whos_turn = 'player_one'
                    self.avail_moves.remove(move)
                    self.moves += 1

                if self.moves == 9:
                    self.game_board.draw_board()
                    print("\nTie game! Close one...")
                    self.game_over = True

            while True:
                again = input("Would you like to play again? (y/n): ")
                if again == 'y':
                    self.game_over = False
                    self.moves = 0
                    self.avail_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    self.game_board.reset_board()
                    break
                elif again == 'n':
                    exit()
                else:
                    print('Invalid answer, try again...')

    def get_opponent(self):
        '''Set the opponent of the game to the computer or another user'''
        while True:
            play_computer = input(f"{self.player_one['name'].capitalize()},"\
                 " would you like to play against the computer? (y/n): ")\
                    .lower().strip()
            if play_computer == 'y':
                self.player_two['name'] = 'computer'
                self.computer_player = True
                break
            elif play_computer == 'n':
                self.player_two['name'] = input("Player two, enter your name: ")
                break
            else:
                print("Cant work with that answer, try again...")

    def get_tokens(self):
        '''Get a valid token choice from player one'''
        while True:
            token = input(f"{self.player_one['name'].capitalize()}, "\
                "do you want to be 'X' or 'O'? (x/o): ").lower().strip()
            if token == 'x':
                self.player_one['token'] = 'x'
                break
            elif token == 'o':
                self.player_one['token'] = 'o'
                break
            else:
                print("Cant work with that answer, try again...")

        if self.player_one['token'] == 'x':
            self.player_two['token'] = 'o'
        else:
            self.player_two['token'] = 'x'

    def get_starting(self):
        '''Get a random starting player'''
        random = randint(1, 2)
        if random == 1:
            self.whos_turn = 'player_one'
        else:
            self.whos_turn = 'player_two'

    def get_move(self, player):
        '''Get a valid move from the current player'''
        while True:
            if player == 'player_one':
                move = input(f"\n{self.player_one['name'].capitalize()}, "\
                        "enter your move! (1-9): ").strip()
                if move == 'q':
                    exit()
                
                try: 
                    move = int(move)
                except ValueError:
                    print("Gotta play by the rules, try again...")
                    continue

                print()
                if move in range(1, 10) and move in self.avail_moves:
                    return move
                else:
                    print("Please enter a valid move, try again...")
            elif player == 'player_two':
                try:
                    move = int(input(f"\n{self.player_two['name'].capitalize()}, "\
                        "enter your move! (1-9): ").strip())
                except ValueError:
                    print("Gotta play by the rules, try again...")
                    continue

                print()
                if move in range(1, 10) and move in self.avail_moves:
                    return move
                else:
                    print("Please enter a valid move, try again...")
    
    def check_status(self):
        '''Check for game status - winner or tie'''
        check = str(self.game_board.check_board_status())
        if check == 'winner':
            if self.whos_turn == 'player_one':
                self.game_board.draw_board()
                print(f"\n{self.player_one['name'].capitalize()}, "\
                    "is the WINNER!")
                self.game_over = True
            elif self.whos_turn == 'player_two':
                self.game_board.draw_board()
                print(f"\n{self.player_two['name'].capitalize()}, "\
                    "is the WINNER!")
                self.game_over = True

    def _draw_logo(self):
        '''Print game logo to the terminal'''
        path = Path('logo.txt')
        contents = path.read_text()
        return contents

game = TicTacToe()
game.main_loop()