class GameBoard:
    '''Represents the Tic Tac Toe game board'''

    def __init__(self):
        '''Initilizes the game board attributes'''
        self.game_board = {
            'top_row': [' 1 ', ' 2 ', ' 3 '],
            'mid_row': [' 4 ', ' 5 ', ' 6 '],
            'btm_row': [' 7 ', ' 8 ', ' 9 '],
        }
    
    def draw_board(self):
        '''Prints the gameboard to the terminal'''
        vert_div = '|'
        hztl_div = '---+---+---'

        for row in self.game_board.keys():
            if row == 'top_row' or row == 'mid_row':
                print(f"\t{self.game_board[row][0]}{vert_div}", end="")
                print(f"{self.game_board[row][1]}{vert_div}", end="")
                print(f"{self.game_board[row][2]}")
                print(f"\t{hztl_div}")
            else:
                print(f"\t{self.game_board[row][0]}{vert_div}", end="")
                print(f"{self.game_board[row][1]}{vert_div}", end="")
                print(f"{self.game_board[row][2]}")

    def update_board(self, move, token):
        '''Update the game board with the provided move'''
        if move in range(1, 4):
            index = move - 1
            self.game_board['top_row'][index] = f" {token.upper()} "
        elif move in range(4, 7):
            index = move - 4
            self.game_board['mid_row'][index] = f" {token.upper()} "
        elif move in range(7, 10):
            index = move - 7
            self.game_board['btm_row'][index] = f" {token.upper()} "

    def check_board_status(self):
        '''Checks for winning combinations on the board'''
        for row in self.game_board.keys():
            hztl_win = [self.game_board[row][0],\
                self.game_board[row][1], self.game_board[row][2]]
            if self._list_check(hztl_win) == True:
                return 'winner'

        for index in range(0, 3):
            vert_win = [self.game_board['top_row'][index],\
                self.game_board['mid_row'][index], self.game_board['btm_row'][index]]
            if self._list_check(vert_win) == True:
                return 'winner'
        
        diag_win_left = [self.game_board['top_row'][0],\
            self.game_board['mid_row'][1], self.game_board['btm_row'][2]]
        if self._list_check(diag_win_left) == True:
            return 'winner'

        diag_win_right = [self.game_board['top_row'][2],\
            self.game_board['mid_row'][1], self.game_board['btm_row'][0]]
        if self._list_check(diag_win_right) == True:
            return 'winner'

    def _list_check(self, list):
        '''Check if all elements in the provided list are the same'''
        elm = list[0]
        chk = True
        for item in list:
            if elm != item:
                chk = False

        if chk == True:
            return True
        elif chk == False:
            return False

    def reset_board(self):
        '''Resets board attributes'''
        self.game_board = {
            'top_row': [' 1 ', ' 2 ', ' 3 '],
            'mid_row': [' 4 ', ' 5 ', ' 6 '],
            'btm_row': [' 7 ', ' 8 ', ' 9 '],
        }