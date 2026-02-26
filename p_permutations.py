# Chapter P ⇒ Permutations

from typing import *


from collections import namedtuple

PE = namedtuple('PD', ['perm', 'elems'])
def permutations(n: int) -> List[List[int]]:
  stack = [PE(perm=[], elems=list(range(1, n + 1)))]
  permutations = []
  while stack:
    perm, elems = stack.pop()
    if not elems:
      permutations.append(perm)
      continue

    for i in range(len(elems)):
      stack.append(
        PE(perm=perm + [elems[i]],
           elems=elems[:i] + elems[i + 1:]),
      )

  return permutations

print('# All permutations')
print('n=3:', permutations(3))  # ==>
# n=3: [
#   [3, 2, 1],
#   [3, 1, 2],
#   [2, 3, 1],
#   [2, 1, 3],
#   [1, 3, 2],
#   [1, 2, 3],
# ]


def permutations_elems(elems: List) -> List[List[int]]:
  stack = [PE(perm=[], elems=elems)]

  permutations = []
  while stack:
    perm, elems = stack.pop()
    if not elems:
      permutations.append(perm)
      continue

    for i in range(len(elems)):
      stack.append(
        PE(perm=perm + [elems[i]],
           elems=elems[:i] + elems[i + 1:]),
      )

  return permutations

print('Custom 1:', permutations_elems([2,3,5]))  # ==>
# Custom 1: [
#   [5, 3, 2],
#   [5, 2, 3],
#   [3, 5, 2],
#   [3, 2, 5],
#   [2, 5, 3],
#   [2, 3, 5],
# ]
print('Custom 2:', permutations_elems(['foo','bar','car']))  # ==>
# Custom 2: [
#   ['car', 'bar', 'foo'],
#   ['car', 'foo', 'bar'],
#   ['bar', 'car', 'foo'],
#   ['bar', 'foo', 'car'],
#   ['foo', 'car', 'bar'],
#   ['foo', 'bar', 'car'],
# ]


def next_perm(perm: List[int]) -> List[int]:
  n = len(perm)
  ix = n - 2
  while ix >= 0:
    if perm[ix] < perm[ix + 1]:
      pivot = perm[ix]
      new_pivot = min(v for v in perm[ix:] if v > pivot)
      new_tail = list(sorted(
        v for v in perm[ix:] if v != new_pivot
      ))
      perm = perm[:ix] + [new_pivot] + new_tail
      break

    ix -= 1

  if ix == -1:
    perm.sort()

  return perm


def previous_perm(perm: List[int]) -> List[int]:
  n = len(perm)
  ix = n - 2
  while ix >= 0:
    if perm[ix] > perm[ix + 1]:
      pivot = perm[ix]
      new_pivot = max(v for v in perm[ix:] if v < pivot)
      new_tail = list(reversed(sorted(
        v for v in perm[ix:] if v != new_pivot
      )))
      perm = perm[:ix] + [new_pivot] + new_tail
      break

    ix -= 1

  if ix == -1:
    perm.sort()
    perm.reverse()

  return perm

print('\n# Generate next and previous premutations')
print(f'{"previous":>9}    {"current":>9}    {"next":>9}')
perm = [1,2,3]
for i in range(6):
  old_p = perm[:]
  next_p = next_perm(old_p[:])
  prev_p = previous_perm(old_p[:])
  print(f'{prev_p} <- {old_p} -> {next_p}')
  perm = next_p
  # 'previous      current         next'
  # [3, 2, 1] <- [1, 2, 3] -> [1, 3, 2]
  # [1, 2, 3] <- [1, 3, 2] -> [2, 1, 3]
  # [1, 3, 2] <- [2, 1, 3] -> [2, 3, 1]
  # [2, 1, 3] <- [2, 3, 1] -> [3, 1, 2]
  # [2, 3, 1] <- [3, 1, 2] -> [3, 2, 1]
  # [3, 1, 2] <- [3, 2, 1] -> [1, 2, 3]
