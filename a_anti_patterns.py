# Chapter A ⇒ Anti-Patterns

from typing import *


# 1. The "Enterprise Architect" (Over-Engineered & Abstraction-Heavy)
class SummationResult:
  def __init__(self, triplets: Set[Tuple[int, ...]]):
    self._data = triplets

  def get_standardized(self) -> List[List[int]]:
    return [list(t) for t in self._data]

class TripleSumValidator:
  TARGET = 0
  @staticmethod
  def validate(a: int, b: int, c: int) -> bool:
    return sum([a, b, c]) == TripleSumValidator.TARGET

def solve_3sum_enterprise(nums: List[int]) -> List[List[int]]:
  nums.sort()
  results = set()
  length = len(nums)

  for i in range(length):
    for j in range(i + 1, length):
      for k in range(j + 1, length):
        if TripleSumValidator.validate(nums[i], nums[j], nums[k]):
          triplet = tuple(sorted((nums[i], nums[j], nums[k])))
          results.add(triplet)

  container = SummationResult(results)
  return container.get_standardized()


# 2. The "C-Programmer in Python" (Manual Memory & Mutation)
def solve_3sum_manual(nums):
  n = len(nums)
  nums.sort()
  res = []

  i = 0
  while i < n - 2:
    if i > 0 and nums[i] == nums[i-1]:
      i += 1
      continue

    l, r = i + 1, n - 1
    while l < r:
      s = nums[i] + nums[l] + nums[r]
      if s < 0:
        l += 1
      elif s > 0:
        r -= 1
      else:
        res.append([nums[i], nums[l], nums[r]])
        while l < r and nums[l] == nums[l+1]: l += 1
        while l < r and nums[r] == nums[r-1]: r -= 1
        l += 1; r -= 1
    i += 1

  return res


# 3. The "Functional Zealot" (One-Liner Obsession)
from itertools import combinations
def solve_3sum_functional(nums):
  return [list(t) for t in {tuple(sorted(c)) for c in combinations(nums, 3) if sum(c) == 0}]


def word_ladder(a: str, b: str, words: List[str]) -> bool:
  if len(a) != len(b): return False

  queue = [a]
  while queue:
    word = queue.pop(0)
    if word == b: return True
    for i in range(len(word)):
      for ch in string.ascii_lowercase:
        new_word = word[:i] + ch + word[i + 1:]
        if new_word != word and new_word in words:
          queue.append(new_word)

  return False


def word_ladder(a, b, d):
  if len(a) != len(b): return False

  q = [a]
  while q:
    w = q.pop(0)
    if w == b: return True
    for i in range(len(w)):
      for c in string.ascii_lowercase:
        n = w[:i] + c + w[i + 1:]
        if n != w and n in d:
          q.append(n)

  return False


VALUES = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
}

def convert_roman(roman):
  VALUES={'I':1,'V':5,'X':10,'L':50,'C':100}
  ret = 0
  for i in range(len(roman)):
    value = VALUES[roman[i]]
    if (i + 1 < len(roman) and
        VALUES[roman[i + 1]] > value):
      value *= -1

    ret += value

  return ret

def convert_roman(roman):
  VALUES={'I':1,'V':5,'X':10,'L':50,'C':100}
  decimal = 0
  for i in range(len(roman)):
    value = VALUES[roman[i]]
    if (i + 1 < len(roman) and
        VALUES[roman[i + 1]] > value):
      value *= -1

    decimal += value

  return decimal

for roman in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XIV', 'XIX', 'XCVIII']:
  print('roman', roman, ':', convert_roman(roman))


def mat2str(mat: List[List[int]]) -> str:
  """Converts a matrix to a dense string:

  10101
  00101
  00001
  """
  return '\n'.join(
    ''.join(str(__) for __ in _)
    for _ in mat
  )


def mat2str(mat: List[List[int]]) -> str:
  """Converts a matrix to a dense string:

  10101
  00101
  00001
  """
  return '\n'.join(
    ''.join(str(cell) for cell in row)
    for row in mat
  )


def mat2str3(mat: List[List[int]]) -> str:
  """Converts a matrix to a dense string:

  10101
  00101
  00001
  """
  lines = []
  for row in mat:
    lines.append(''.join(str(cell) for cell in row))

  return '\n'.join(lines)


print(list(
  (x, y, z)
  for x in range(3)
  for y in range(3)
  if x <= y
  for z in range(3)
  if y != z
))


def twosum_sort(
  nums: List[int], target: int,
) -> List[int]:
  nums.sort()
  i, j = 0, len(nums) - 1
  while i < j:
    value = nums[i] + nums[j]
    if value == target:
      return [nums[i], nums[j]]
    elif value < target:
      i += 1
    else:
      j -= 1

  return None


def f(n,t):
  n.sort()
  while n:
    v=n[0]+n[-1]
    if v==t: return n[0],n[-1]
    n.pop(0 if v<t else -1)

print('twosum_sort:', twosum_sort([7,4,8,2,1,9,3], 13))
# twosum_brute: [4, 9]
print('Code golf:', f([7,4,8,2,1,9,3], 13))
