# Chapter F ⇒ Flood Fill

from typing import *


matrix = [
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,1,0],
  [0,0,1,1,0,0,0,0,0,0],
  [0,0,1,0,1,0,0,0,0,0],
  [0,1,1,1,0,1,1,0,0,0],
  [0,1,0,1,0,1,1,1,0,0],
  [0,0,0,0,0,0,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0],
]

def to_str(mat):
  return '\n'.join(
    ''.join(str(c) if c else '.' for c in row)
    for row in mat
  )

print('# Paint bucket')
print('With matrix:')
print(to_str(matrix))
# ..........
# ........1.
# ..11......
# ..1.1.....
# .111.11...
# .1.1.111..
# ......11..
# ..........


def flood_fill_4neighborhood(matrix, r, c, color):
  old_color = matrix[r][c]
  m = len(matrix)
  n = len(matrix[0])

  def inner(rr, cc):
    if matrix[rr][cc] != old_color:
      return

    matrix[rr][cc] = color
    if rr:
      inner(rr - 1, cc)
    if rr + 1 < m:
      inner(rr + 1, cc)
    if cc:
      inner(rr, cc - 1)
    if cc + 1 < n:
      inner(rr, cc + 1)

  inner(r, c)

flood_fill = flood_fill_4neighborhood


import copy

mat1 = copy.deepcopy(matrix)
flood_fill_4neighborhood(mat1, 2, 2, 2)
print('Flood fill 4-connected at (2,2):')
print(to_str(mat1))
# Flood fill 4-connected at (2,2):
# ..........
# ........1.
# ..22......
# ..2.1.....
# .222.11...
# .2.2.111..
# ......11..
# ..........


def flood_fill_8neighborhood(matrix, r, c, color):
  old_color = matrix[r][c]
  m = len(matrix)
  n = len(matrix[0])

  def inner(rr, cc):
    if matrix[rr][cc] != old_color:
      return

    matrix[rr][cc] = color
    for dr in (-1, 0, 1):
      for dc in (-1, 0, 1):
        if dr or dc:
          r_new = rr + dr
          c_new = cc + dc
          if 0 <= r_new < m and 0 <= c_new < n:
            inner(r_new, c_new)

  inner(r, c)

mat2 = copy.deepcopy(matrix)
flood_fill_8neighborhood(mat2, 2, 2, 2)
print('Flood fill 8-connected at (2,2):')
print(to_str(mat2))
# Flood fill 8-connected at (2,2):
# ..........
# ........1.
# ..22......
# ..2.2.....
# .222.22...
# .2.2.222..
# ......22..
# ..........


def count_islands(matrix):
  m = len(matrix)
  n = len(matrix[0])
  num_islands = 0
  for r in range(m):
    for c in range(n):
      if matrix[r][c] == 1:
        num_islands += 1
        flood_fill(matrix, r, c, 0)

  return num_islands

print('\n# Count islands')
mat3 = copy.deepcopy(matrix)
print('Num islands:', count_islands(mat3))
# Num islands: 4


def flood_fill_count(matrix, r, c, color):
  old_color = matrix[r][c]
  m = len(matrix)
  n = len(matrix[0])

  def inner(rr, cc):
    if not (0 <= rr < m and 0 <= cc < n):
      return 0
    if matrix[rr][cc] != old_color:
      return 0

    matrix[rr][cc] = color
    return (
      1 +
      inner(rr - 1, cc) +
      inner(rr + 1, cc) +
      inner(rr, cc - 1) +
      inner(rr, cc + 1)
    )

  return inner(r, c)


def find_largest_island(matrix):
  m = len(matrix)
  n = len(matrix[0])
  largest_island = 0
  for r in range(m):
    for c in range(n):
      if matrix[r][c] == 1:
        largest_island = max(
          largest_island,
          flood_fill_count(matrix, r, c, 0)
        )

  return largest_island

mat4 = copy.deepcopy(matrix)
print('Largest area:', find_largest_island(mat4))
# Largest area: 8


def flood_fill_perimeter(matrix, r, c, color):
  old_color = matrix[r][c]
  m = len(matrix)
  n = len(matrix[0])

  def inner(rr, cc):
    if not (0 <= rr < m and 0 <= cc < n):
      return 0
    if matrix[rr][cc] != old_color:
      return 0

    matrix[rr][cc] = color
    is_perimeter = (
      (rr > 0 and matrix[rr - 1][cc] == 0) or
      (rr + 1 < m and matrix[rr + 1][cc] == 0) or
      (cc > 0 and matrix[rr][cc - 1] == 0) or
      (cc + 1 < n and matrix[rr][cc + 1] == 0)
    )
    return (
      int(is_perimeter) +
      inner(rr - 1, cc) +
      inner(rr + 1, cc) +
      inner(rr, cc - 1) +
      inner(rr, cc + 1)
    )

  return inner(r, c)


def count_perimeter(matrix):
  m = len(matrix)
  n = len(matrix[0])
  total_perimeter = 0
  for r in range(m):
    for c in range(n):
      if matrix[r][c] == 1:
        total_perimeter += (
          flood_fill_perimeter(matrix, r, c, 2)
        )

  return total_perimeter

mat5 = copy.deepcopy(matrix)
print('Perimeter length:', count_perimeter(mat5))
# Perimeter length: 16


def count_true_islands(matrix):
  m = len(matrix)
  n = len(matrix[0])

  for r in range(m):
    if matrix[r][0] == 1:
      flood_fill(matrix, r, 0, 0)
    if matrix[r][-1] == 1:
      flood_fill(matrix, r, n - 1, 0)

  for c in range(n):
    if matrix[0][c] == 1:
      flood_fill(matrix, 0, c, 0)
    if matrix[-1][c] == 1:
      flood_fill(matrix, m - 1, c, 0)

  num_islands = 0
  for r in range(m):
    for c in range(n):
      if matrix[r][c] == 1:
        num_islands += 1
        flood_fill(matrix, r, c, 0)

  return num_islands

print('\n# Excluding continents')
mat6 = [
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 0],
]
print('With map:')
# With map:
# ....
# .11.
# .11.
# ....
print(to_str(mat6))
print('Num true islands:', count_true_islands(mat6))
# Num true islands: 1

mat7 = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 1],
]
print('With map:')
# With map:
# .....
# .111.
# .111.
# .111.
# ....1
print(to_str(mat7))
print('Num true islands:', count_true_islands(mat7))
# Num true islands: 1

mat8 = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0],
]
print('With map:')
# With map:
# .....
# .111.
# .1.1.
# 11...
# .....
print(to_str(mat8))
print('Num true islands:', count_true_islands(mat8))
# Num true islands: 0
