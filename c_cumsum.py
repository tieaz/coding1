# Chapter C ⇒ Cumsum

from typing import *


def reservoir_volume(terrain: List[int]) -> int:
  pass


print('# Reservoir volume')
terrain = [1, 3, 1, 1, 2, 0, 0, 1, 2, 2, 4, 1]
print('Sample terrain:', terrain)

def reservoir_volume_brute(terrain: List[int]) -> int:
  water_height = terrain[:]
  for i in range(len(terrain)):

    water_height[i] = min(max(terrain[:i + 1]), max(terrain[i:])) - terrain[i]

  return sum(water_height)

print('Brute force solution:', reservoir_volume_brute(terrain))
# Brute force solution: 15


def reservoir_volume_cumsum(terrain: List[int]) -> int:
  cumleft = [terrain[0]]
  for i in range(1, len(terrain)):
    cumleft.append(max(terrain[i], cumleft[-1]))

  cumright = [terrain[-1]]
  for i in range(len(terrain) - 2, -1, -1):
    cumright.append(max(terrain[i], cumright[-1]))

  cumright = cumright[::-1]

  return sum([
    min(cumleft[i], cumright[i]) - terrain[i]
    for i in range(len(terrain))
  ])

print('Cumsum solution:', reservoir_volume_cumsum(terrain))
# Cumsum solution: 15


class RangeSumQuery(object):
  def __init__(self, arr: List[int]):
    self.arr = arr
    self.cumsum = [arr[0]] * len(arr)
    for i in range(1, len(arr)):
      self.cumsum[i] = self.cumsum[i - 1] + arr[i]

  def query(self, left: int, right: int) -> int:
    return self.cumsum[right] - (self.cumsum[left - 1] if left else 0)

print('\n# Range sum query')
arr = [1, -2, 0, 3, 5, 2, -1]
print('Given array:', arr)
range_sum = RangeSumQuery(arr)
print('Range [0,5]:', range_sum.query(0, 5))
# Range [0,5]: 9
print('Range [1,5]:', range_sum.query(1, 5))
# Range [1,5]: 8
print('Range [2,5]:', range_sum.query(2, 5))
# Range [2,5]: 10
print('Range [3,5]:', range_sum.query(3, 5))
# Range [3,5]: 10
print('Range [4,5]:', range_sum.query(4, 5))
# Range [4,5]: 7
print('Range [5,5]:', range_sum.query(5, 5))
# Range [5,5]: 2


print('\n# Range sum query 2D')
matrix = [
  [1, 3, 2, 6, 2, 0],
  [5, 4, 2, 0, 1, 6],
  [1, 3, 2, 6, 2, 0],
  [5, 4, 2, 0, 1, 6],
]
print('matrix:', matrix)

m = len(matrix)
n = len(matrix[0])
cummatrix = [[0] * n for i in range(m)]
for r in range(m):
  cummatrix[r][0] = matrix[r][0]
  for c in range(1, n):
    cummatrix[r][c] = cummatrix[r][c - 1] + matrix[r][c]

for r in range(1, m):
  for c in range(n):
    cummatrix[r][c] += cummatrix[r - 1][c]

print('cummatrix:', cummatrix)
# cummatrix: [
#   [1, 4, 6, 12, 14, 14],
#   [6, 13, 17, 23, 26, 32],
#   [7, 17, 23, 35, 40, 46],
#   [12, 26, 34, 46, 52, 64],
# ]

r1, c1 = 1, 1
r2, c2 = 3, 3
sum_range = (
  cummatrix[r2][c2] -
  (cummatrix[r2][c1 - 1] if c1 else 0) -
  (cummatrix[r1 - 1][c2] if r1 else 0) +
  (cummatrix[r1 - 1][c1 - 1] if r1 and c1 else 0)
)
print('Range sum query 2D', r1, c1, r2, c2, ':', sum_range)
# Range sum query 2D 1 1 3 3 : 23


print('\n# Product of array except self')
values = [1, 2, 3, 4]
values = [-1, 1, 0, -3, 3]

cumleft = [1]
for i in range(0, len(values) - 1):
  cumleft.append(cumleft[-1] * values[i])

cumright = [1]
for i in range(len(values) - 1, 0, -1):
  cumright.append(cumright[-1] * values[i])

cumright = cumright[::-1]
print('cumleft:', cumleft)
# cumleft: [1, -1, -1, 0, 0]
print('cumright:', cumright)
# cumright: [0, 0, -9, 3, 1]

products = [cumleft[i] * cumright[i] for i in range(len(values))]
print('Cum products:', products)
# Cum products: [0, 0, 9, 0, 0]
