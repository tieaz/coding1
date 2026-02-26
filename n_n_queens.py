# Chapter N ⇒ N-Queens

from typing import *

print('# Exhaustive search with n=3')
# n = 3
# for value in range(2 ** n ** 2):
#   board = [['.'] * n for i in range(n)]
#   for j in range(n ** 2):
#     if value & (1 << j):
#       board[j // n][j % n] = 'Q'

#   if True: print('\n'.join(''.join(row) for row in board))

n = 3
lines = []
for value in range(2 ** n ** 2):
  if not value % 32:
    if value: lines.append('')
    lines.append('')
    lines.append('')
    lines.append('')

  board = [['.'] * n for i in range(n)]
  for j in range(n ** 2):
    if value & (1 << j):
      board[j // n][j % n] = 'Q'

  # print('\n' + '\n'.join(''.join(row) for row in board))
  lines[-3] += (' ' if value % 32 else '') + ''.join(board[0])
  lines[-2] += (' ' if value % 32 else '') + ''.join(board[1])
  lines[-1] += (' ' if value % 32 else '') + ''.join(board[2])

if True:
  print('\n'.join(lines))


import copy
from collections import namedtuple


def is_valid(board: List[List[str]]) -> bool:
  n = len(board)
  rows, cols, diags, anti_diags = set(), set(), set(), set()
  num_queens = 0
  for r in range(n):
    for c in range(n):
      if board[r][c] == 'Q':
        num_queens += 1
        rows.add(r)
        cols.add(c)
        diags.add(c - r)
        anti_diags.add(n - 1 - c - r)

  return (
    len(rows) == len(cols) == len(diags) == len(anti_diags) == num_queens
  )


BC = namedtuple('BC', ['board', 'col'])
def n_queens(n: int) -> str:
  stack = [BC(board=[['.'] * n for i in range(n)], col=0)]
  while stack:
    board, col = stack.pop()
    if col == n:
      return '\n'.join(''.join(row) for row in board)

    for row in range(n):
      new_board = copy.deepcopy(board)
      new_board[row][col] = 'Q'
      if is_valid(new_board):
        stack.append(BC(board=new_board, col=col + 1))

  return None

print('\n# N-queens')
print('n=3:')
print(n_queens(3))
# n=3:
# None

print('\nn=4:')
print(n_queens(4))
# n=4:
# .Q..
# ...Q
# Q...
# ..Q.

print('\nn=8:')
print(n_queens(8))
# n=8:
# ..Q.....
# .....Q..
# ...Q....
# .Q......
# .......Q
# ....Q...
# ......Q.
# Q.......

print('\nn=9:')
print(n_queens(9))
# n=9:
# ......Q..
# ...Q.....
# .......Q.
# ..Q......
# ........Q
# .....Q...
# .Q.......
# ....Q....
# Q........


KNIGHT_DIALING = {
  0: [4, 6],
  1: [6, 8],
  2: [7, 9],
  3: [4, 8],
  4: [3, 9, 0],
  5: [],
  6: [1, 7, 0],
  7: [2, 6],
  8: [1, 3],
  9: [2, 4],
}

def knight_dialer(n: int) -> List[str]:
  if not n: return []
  stack = [[i] for i in range(10)]
  solutions = []
  while stack:
    number = stack.pop()
    if len(number) == n:
      solutions.append(number)
      continue

    for next_num in KNIGHT_DIALING[number[-1]]:
      stack.append(number + [next_num])

  return solutions

print('\n# Knight dialing')
print('n=1:', knight_dialer(1))
# n=1: [[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]]
print('n=2:', knight_dialer(2))
# n=2: [[9, 4], [9, 2], [8, 3], [8, 1], [7, 6], [7, 2], [6, 0], [6, 7], [6, 1], [4, 0], [4, 9], [4, 3], [3, 8], [3, 4], [2, 9], [2, 7], [1, 8], [1, 6], [0, 6], [0, 4]]
print('Num n=3:', len(knight_dialer(3)))
# Num n=3: 46
print('Num n=10:', len(knight_dialer(10)))
# Num n=10: 14912


def knight_dialer_count(n: int) -> int:
  combos = [1] * 10
  for gen in range(n - 1):
    new_combos = [0] * 10
    for digit in range(10):
      new_combos[digit] = sum(
        combos[d] for d in KNIGHT_DIALING[digit]
      )

    combos = new_combos

  return sum(combos)

print('\n# Knight dialer count')
print('n=100:', knight_dialer_count(100))
# n=100: 3378871863861577026028284154474397696
