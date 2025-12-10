
### Water height O(n^2) solution

terrain = [1, 3, 1, 1, 2, 0, 0, 1, 2, 2, 4, 1]

water_height = terrain[:]
for i in range(len(terrain)):
  water_height[i] = min(max(terrain[:i + 1]), max(terrain[i:])) - terrain[i]

print('Solution 1:', sum(water_height))


### Water height O(n) cumsum solution

cumleft = [terrain[0]]
for i in range(1, len(terrain)):
  cumleft.append(max(terrain[i], cumleft[-1]))

cumright = [terrain[-1]]
for i in range(len(terrain) - 2, -1, -1):
  cumright.append(max(terrain[i], cumright[-1]))

cumright = cumright[::-1]

water_height = [
  min(cumleft[i], cumright[i]) - terrain[i]
  for i in range(len(terrain))
]
print('\ncumleft:', cumleft)
print('cumright:', cumright)
print('Solution 2:', sum(water_height))


### Cumulative product

values = [1, 2, 3, 4]
values = [-1, 1, 0, -3, 3]

cumleft = [1]
for i in range(0, len(values) - 1):
  cumleft.append(cumleft[-1] * values[i])

cumright = [1]
for i in range(len(values) - 1, 0, -1):
  cumright.append(cumright[-1] * values[i])

cumright = cumright[::-1]

products = [cumleft[i] * cumright[i] for i in range(len(values))]
print('\nCum products:', products)


### Range Sum Query 2D

matrix = [
  [1, 3, 2, 6, 2, 0],
  [5, 4, 2, 0, 1, 6],
  [1, 3, 2, 6, 2, 0],
  [5, 4, 2, 0, 1, 6],
]

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

r1, c1 = 1, 1
r2, c2 = 3, 3
sum_range = (
  cummatrix[r2][c2] -
  (cummatrix[r2][c1 - 1] if c1 else 0) -
  (cummatrix[r1 - 1][c2] if r1 else 0) +
  (cummatrix[r1 - 1][c1 - 1] if r1 and c1 else 0)
)
print('\nRange sum query 2D', r1, c1, r2, c2, ':', sum_range)
