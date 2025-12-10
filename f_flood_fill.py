
def to_str(mat):
  return '/'.join(''.join(str(_) for _ in row) for row in mat)

def test_flood_fill4(func):
  mat = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
  ]

  assert to_str(mat) == '010/111/010'
  func(mat, 0, 0, 1)
  assert to_str(mat) == '110/111/010'
  func(mat, 1, 1, 2)
  assert to_str(mat) == '220/222/020'
  print('PASSED!')


def test_flood_fill8(func):
  mat = [
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 1],
  ]

  assert to_str(mat) == '010/100/001'
  func(mat, 0, 1, 2)
  assert to_str(mat) == '020/200/001'
  func(mat, 1, 1, 2)
  assert to_str(mat) == '222/222/221'
  print('PASSED!')


### Flood fill with check-then-recurse

def flood_fill(matrix, r, c, color):
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

matrix = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 2, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

flood_fill(matrix, 0, 2, 3)
print('Basic flood fill:')
print('\n'.join(str(_) for _ in matrix))
test_flood_fill4(flood_fill)


### Flood fill with recurse-then-check

def flood_fill_rtc(matrix, r, c, color):
  old_color = matrix[r][c]
  m = len(matrix)
  n = len(matrix[0])

  def inner(rr, cc):
    if not (0 <= rr < m and 0 <= cc < n):
      return
    if matrix[rr][cc] != old_color:
      return

    matrix[rr][cc] = color

    inner(rr - 1, cc)
    inner(rr + 1, cc)
    inner(rr, cc - 1)
    inner(rr, cc + 1)

  inner(r, c)

print('\nflood_fill_rtc:')
test_flood_fill4(flood_fill_rtc)


### Flood fill with 8-neighborhood

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

print('\nflood_fill_8neighborhood:')
test_flood_fill8(flood_fill_8neighborhood)


### Count islands

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

def test_count_islands(func):
  mat = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ]
  assert func(mat) == 2
  print('PASSED!')

print('\ncount islands:')
test_count_islands(count_islands)


### Flood fill with count

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

def test_flood_fill4_count(func):
  mat = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
  ]

  assert to_str(mat) == '010/111/010'
  assert func(mat, 0, 0, 1) == 1
  assert to_str(mat) == '110/111/010'
  assert func(mat, 1, 1, 2) == 6
  assert to_str(mat) == '220/222/020'
  print('PASSED!')


print('\nflood_fill_count:')
test_flood_fill4_count(flood_fill_count)


### Find largest island

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

def test_find_largest_island(func):
  mat = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ]
  assert func(mat) == 3
  print('PASSED!')

print('\nfind_largest_island:')
test_find_largest_island(find_largest_island)


### Flood fill and count perimeter

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

def count_perimter(matrix):
  m = len(matrix)
  n = len(matrix[0])
  total_perimeter = 0
  for r in range(m):
    for c in range(n):
      if matrix[r][c] == 1:
        total_perimeter += flood_fill_perimeter(matrix, r, c, 2)

  return total_perimeter

def test_count_perimter(func):
  mat = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
  ]
  assert func(mat) == 4

  mat = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
  ]
  assert func(mat) == 8

  mat = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
  ]
  assert func(mat) == 7

  mat = [
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
  ]
  assert func(mat) == 8
  print('PASSED!')

print('\ncount_perimter:')
test_count_perimter(count_perimter)


### Count true islands (non-continents)

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

def test_count_true_islands(func):
  mat = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
  ]
  assert func(mat) == 1

  mat = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
  ]
  assert func(mat) == 1

  mat = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
  ]
  assert func(mat) == 0
  print('PASSED!')

print('\ncount_true_islands:')
test_count_true_islands(count_true_islands)
