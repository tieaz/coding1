# Chapter S ⇒ *SUM

from typing import *


def twosum_brute(
  nums: List[int], target: int,
) -> List[int]:
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [nums[i], nums[j]]

  return None

print('# 2SUM')
arr = [7,4,8,2,1,9,3]
target = 13
print(f'Given array: {arr} and target: {target}')  # ==>
# Given array: [7, 4, 8, 2, 1, 9, 3] and target: 13
print('2SUM brute force:', twosum_brute(arr, 13))  # ==>
# 2SUM brute force: [4, 9]


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

print(f'Given array: {arr} and target: {target}')  # ==>
# Given array: [7, 4, 8, 2, 1, 9, 3] and target: 13
print('2SUM sort:', twosum_sort(arr, target))
# 2SUM sort: [4, 9]


from collections import namedtuple

ValIx = namedtuple('ValIx', ['val', 'ix'])


print('# 2SUM non-destructive')
nums = [7,4,8,2,1,9,3]
print('Given array:', nums)
nums_ix = [
  (nums[i], i) for i in range(len(nums))
]
print('Paired with indices:', nums_ix)  # ==>
# Paired with indices: [(7, 0), (4, 1), (8, 2), (2, 3), (1, 4), (9, 5), (3, 6)]

nums_ix.sort()
print('Sorted:', nums_ix)  # ==>
# Sorted: [(1, 4), (2, 3), (3, 6), (4, 1), (7, 0), (8, 2), (9, 5)]

sorted_nums, ixes = zip(*nums_ix)
print("Zip'ed back out:", sorted_nums, ixes)  # ==>
# Zip'ed back out: (1, 2, 3, 4, 7, 8, 9) (4, 3, 6, 1, 0, 2, 5)


def twosum_sorted(nums: List[int], target: int) -> List[int]:
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


def threesum_twosum(nums: List[int]) -> List[int]:
  nums.sort()
  for i in range(len(nums) - 2):
    twosum_sol = twosum_sorted(nums[i + 1:], -nums[i])
    if twosum_sol:
      return [nums[i]] + twosum_sol

  return None


def threesum(nums: List[int]) -> List[int]:
  nums.sort()
  for i in range(len(nums) - 2):
    j = i + 1
    k = len(nums) - 1
    while j < k:
      target = nums[i] + nums[j] + nums[k]
      if target == 0:
        return [nums[i], nums[j], nums[k]]
      elif target < 0:
        j +=1
      else:
        k -= 1

  return None

print('\n# 3SUM')
nums = [-3,2,-1,1,3,-6]
print('Given array:', nums)
print('3SUM solution:', threesum(nums))  # ==>
# 3SUM solution: [-3, 1, 2]
print('3SUM with 2SUM reduction', threesum_twosum(nums))  # ==>
# 3SUM with 2SUM reduction [-3, 1, 2]


def threesum_solutions(
  nums: List[int],
) -> List[Tuple[int]]:
  nums.sort()
  solutions = set()
  for i in range(len(nums) - 2):
    j = i + 1
    k = len(nums) - 1
    while j < k:
      target = nums[i] + nums[j] + nums[k]
      if target == 0:
        solutions.add((nums[i], nums[j], nums[k]))
        j += 1
        k -= 1
      elif target < 0:
        j +=1
      else:
        k -= 1

  return list(solutions)

nums = [-3,2,-1,1,4,-6]
print('Given array:', nums)
print('3SUM solutions:', threesum_solutions(nums))  # ==>
# 3SUM solutions: [(-3, -1, 4), (-6, 2, 4), (-3, 1, 2)]


def foursum(nums: List[int]) -> List[List[int]]:
  pairs = {}
  for i in range(len(nums) - 1):
      for j in range(i + 1, len(nums)):
          value = nums[i] + nums[j]
          pairs.setdefault(value, []).append((i, j))

  solutions = set()
  for sum1, ixes1 in pairs.items():
    ixes2 = pairs.get(-sum1, [])
    for i1, j1 in ixes1:
      for i2, j2 in ixes2:
        if len(set([i1, j1, i2, j2])) == 4:
          solutions.add(
            tuple(sorted([nums[i1], nums[j1], nums[i2], nums[j2]]))
          )

  return list(solutions)

print('\n# 4SUM')
nums = [1,0,-1,-2,2]
print('Given array:', nums)
pairs = {
  -3: [(2, 3)],
  -2: [(1, 3)],
  -1: [(0, 3), (1, 2)],
  0: [(0, 2), (3, 4)],
  1: [(0, 1), (2, 4)],
  2: [(1, 4)],
  3: [(0, 4)],
}
print('4SUM:', foursum(nums))  # ==>
# 4SUM: [(-2, -1, 1, 2)]
