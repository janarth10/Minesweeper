from pprint import pprint

M = N = 4
MINE = 'X'
NUM_MINES = 3
class Board:
    def __init__(self):
        self._board = [[{'covered': True, 'val': 0} for _ in range(N)] for _ in range(M)]
        self._assign_mines()
        self._get_cell_vals()
        self._uncovered_cells = set()
        self._gameOver = False

    def _assign_mines(self):
        # TODO make it random
        self._board[0][2]['val'] = MINE
        self._board[2][1]['val'] = MINE
        self._board[3][3]['val'] = MINE

    def _print_board(self):
        for i in range(M):
            for j in range(N):
                cell = self._board[i][j]
                if cell['covered']:
                    print('{0:<5}'.format('C'), end='')
                else:
                    print('{0:<5}'.format(cell['val']), end='')
            print()

    def _get_cell_vals(self):
        d = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        for i in range(M):
            for j in range(N):
                if self._board[i][j]['val'] == MINE: continue
                val = 0
                for di, dj in d:
                    val += self._is_mine(i+di, j+dj)
                self._board[i][j]['val'] = val

    def _is_valid(self, row, col):
        return row >= 0 and row < M and col >= 0 and col < N

    def _is_mine(self, row, col):
        return self._is_valid(row, col) and self._board[row][col]['val'] == MINE

    def _failed(self):
        self._gameOver = True
        print('failed try again')

    def _succeeded(self):
        self._gameOver = True
        print('Game Won!')

    def isGameOver(self):
        # TODO check state of board
        return self._gameOver

    def click_cell(self, row, col):
        print('clicked {}, {}'.format(row,col))
        if not self._is_valid(row, col):
            print("Cell coordinates are invalid!")
        elif (row, col) in self._uncovered_cells:
            print("Cell already clicked!")
        elif self._is_mine(row, col):
            self._failed()
        else:
            # TODO add function to handle uncovering cells
            self._board[row][col]['covered'] = False
            self._uncovered_cells.add((row,col))
            if len(self._uncovered_cells) == N*M-NUM_MINES:
                self._succeeded()

board = Board()
while not board.isGameOver():
    board._print_board()
    cellClicked = input("Input row and column of cell you wish to click!")
    rowCol = [int(s) for s in cellClicked.split()]
    board.click_cell(*rowCol)
# board.endGame()
