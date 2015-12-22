from models.move import Move
import copy

class Board:
  EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'

  UP, DOWN, LEFT, RIGHT = [-1, 0], [1, 0], [0, -1], [0, 1]
  UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = [-1, 1], [1, 1], [1, -1], [-1, -1]

  DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

  def __init__(self, board):
    if board is None:
      self.board = []
      for i in range(0, 10):
        self.board.insert(i, [Board.OUTER]*10)

      for i in range(1, 9):
        for j in range(1, 9):
          self.board[i][j] = Board.EMPTY

      self.board[4][4], self.board[4][5] = Board.WHITE, Board.BLACK
      self.board[5][4], self.board[5][5] = Board.BLACK, Board.WHITE
    else:
      self.board = copy.deepcopy(board)

  def play(self, move, color):
    if (color == Board.BLACK) or (color == Board.WHITE):
      self.board[move.x][move.y] = color
      self._reverse(move, color)
    return
    
  def get_square_color(self,l,c):
    return self.board[l][c]

  def get_clone(self):
    return Board(self.board)

  def valid_moves(self, color):
    ret = []
    for i in range(1, 9):
      for j in range(1, 9):
        if self.board[i][j] == Board.EMPTY:
          for direction in Board.DIRECTIONS:
            move = Move(i, j)
            bracket = self._find_bracket(move, color, direction)
            if bracket:
              ret += [move]
    return ret

  def __str__(self):
    ret = 'Score(White, Black): ' + self.score().__str__()
    ret += '\n  '
    for i in range(1, 9):
      ret += i.__str__() + ' '
    ret += '\n'
    for i in range(1, 9):
      ret += i.__str__() + ' '
      for j in range(1, 9):
        ret += self.board[i][j] + ' '
      ret += '\n'
    return ret

  def score(self):
    white = 0
    black = 0
    for i in range(1, 9):
      for j in range(1, 9):
        if self.board[i][j] == Board.WHITE:
          white += 1
        elif self.board[i][j] == Board.BLACK:
          black += 1

    return [white, black]


  def _squares(self):
    return [i for i in xrange(11, 89) if 1 <= (i % 10) <= 8]

  def _reverse(self, move, color):
    for direction in Board.DIRECTIONS:
      self._make_flips(move, color, direction)

  def _make_flips(self, move, color, direction):
    bracket = self._find_bracket(move, color, direction)
    if not bracket:
        return
    square = [move.x + direction[0], move.y + direction[1]]
    while square != bracket:
      self.board[square[0]][square[1]] = color
      square = [square[0] + direction[0], square[1] + direction[1]]

  def _find_bracket(self, move, color, direction):
    bracket = [move.x + direction[0], move.y + direction[1]]
    bracket_color = self.board[bracket[0]][bracket[1]]

    if bracket_color == color:
      return None
    opponent = self._opponent(color)
    while bracket_color == opponent:
      bracket = [bracket[0] + direction[0], bracket[1] + direction[1]]
      bracket_color = self.board[bracket[0]][bracket[1]]

    return None if self.board[bracket[0]][bracket[1]] in (Board.OUTER, Board.EMPTY) else bracket

  def _opponent(self, color):
    return Board.BLACK if color is Board.WHITE else Board.WHITE