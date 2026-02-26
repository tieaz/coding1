# Chapter Q ⇒ Quickselect

from typing import *

def mergesort(arr: List[int]) -> List[int]:
  if len(arr) < 2: return arr
  mid = len(arr) // 2
  left = mergesort(arr[:mid])
  right = mergesort(arr[mid:])
  l, r = 0, 0
  sorted_arr = []
  while l < len(left) and r < len(right):
    if left[l] < right[r]:
      sorted_arr.append(left[l])
      l += 1
    else:
      sorted_arr.append(right[r])
      r += 1

  sorted_arr.extend(left[l:] + right[r:])
  return sorted_arr

print('# Mergesort')
names = ['Alice', 'Bob', ..., 'Zed']
ages = [23, 27, ..., 56]
heights = [167, 185, ..., 155]

arr = [(names[i], ages[i], heights[i]) for i in range(len(names))]
print(arr)  # ==>
# [('Alice', 23, 167), ('Bob', 27, 185), ..., ('Zed', 56, 155)]


print('\n# Zip operations')
names = ['Alice', 'Bob', ..., 'Zed']
ages = [23, 27, ..., 56]
heights = [167, 185, ..., 155]

arr = list(zip(names, ages, heights))
print(arr)  # ==>
# [('Alice', 23, 167), ('Bob', 27, 185), ..., ('Zed', 56, 155)]

n, a, h = zip(*arr)
print(n, a, h)  # ==>
# ('Alice', 'Bob', ..., 'Zed') (23, 27, ..., 56) (167, 185, ..., 155)


print('\n# Composite sorting')
import random

random.seed(20251205)

names = [chr(ord('A') + i) for i in range(26)]
ages = [random.randint(20, 30) for i in range(26)]
heights = [random.randint(100, 150) for i in range(26)]
arr = list(zip(names, ages, heights))
sorted_arr = mergesort(arr)
print(sorted_arr)  # ==>
# [('A', 22, 139), ('B', 28, 121), ('C', 27, 141), ('D', 24, 122), ('E', 25, 102),
#  ('F', 23, 128), ('G', 20, 128), ('H', 20, 116), ('I', 21, 110), ('J', 24, 122),
#  ('K', 26, 100), ('L', 23, 125), ('M', 20, 113), ('N', 28, 126), ('O', 23, 117),
#  ('P', 20, 141), ('Q', 21, 129), ('R', 20, 147), ('S', 23, 146), ('T', 22, 104),
#  ('U', 30, 131), ('V', 22, 144), ('W', 20, 149), ('X', 29, 144), ('Y', 27, 141),
#  ('Z', 29, 108)]


print('\n# Composite sorting with descending sort')
random.seed(20251205)

names = [chr(ord('A') + i) for i in range(26)]
ages = [random.randint(20, 30) for i in range(26)]
heights = [random.randint(100, 150) for i in range(26)]
arr = [(ages[i], -heights[i], names[i]) for i in range(len(names))]
sorted_arr = mergesort(arr)
print(sorted_arr)
# [(20, -149, 'W'), (20, -147, 'R'), (20, -141, 'P'), (20, -128, 'G'), (20, -116, 'H'),
#  (20, -113, 'M'), (21, -129, 'Q'), (21, -110, 'I'), (22, -144, 'V'), (22, -139, 'A'),
#  (22, -104, 'T'), (23, -146, 'S'), (23, -128, 'F'), (23, -125, 'L'), (23, -117, 'O'),
#  (24, -122, 'D'), (24, -122, 'J'), (25, -102, 'E'), (26, -100, 'K'), (27, -141, 'C'),
#  (27, -141, 'Y'), (28, -126, 'N'), (28, -121, 'B'), (29, -144, 'X'), (29, -108, 'Z'),
#  (30, -131, 'U')]

sorted_ages = [x[0] for x in sorted_arr]
sorted_heights = [-x[1] for x in sorted_arr]
sorted_names = [x[2] for x in sorted_arr]


print('\n# Composite sorting with key function')
arr = list(zip(names, ages, heights))
arr.sort(key=lambda x: (x[1], -x[2]))
names, ages, heights = zip(*arr)
print(names)  # ==>
# ('W', 'R', 'P', 'G', 'H', 'M', 'Q', 'I', 'V', 'A', 'T', 'S', 'F', 'L', 'O', 'D', 'J',
#  'E', 'K', 'C', 'Y', 'N', 'B', 'X', 'Z', 'U')
print(ages)  # ==>
# (20, 20, 20, 20, 20, 20, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 26, 27, 27,
#  28, 28, 29, 29, 30)
print(heights)  # ==>
# (149, 147, 141, 128, 116, 113, 129, 110, 144, 139, 104, 146, 128, 125, 117, 122, 122,
#  102, 100, 141, 141, 126, 121, 144, 108, 131)


def dutch_flag(arr):
  zeros = 0
  twos = len(arr) - 1
  i = 0
  while i <= twos:
    if arr[i] == 2:
      arr[i], arr[twos] = arr[twos], arr[i]
      twos -= 1
    elif arr[i] == 0:
      arr[i], arr[zeros] = arr[zeros], arr[i]
      i += 1
      zeros += 1
    else:
      i += 1

print('\n# Dutch national flag')
arr = [2, 1, 0, 1, 1, 0, 2, 2, 0]
print('Given array:', arr)
dutch_flag(arr)
print('Dutch flag sort:', arr)
# [0, 0, 0, 1, 1, 1, 2, 2, 2]


def quicksort(arr: List, lo: int=0, hi: int=None):
  if hi is None: hi = len(arr) - 1
  if lo >= hi: return

  pivot = arr[hi]
  i = lo
  for j in range(lo, hi):
    if arr[j] <= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1

  arr[i], arr[hi] = arr[hi], arr[i]
  quicksort(arr, lo, i - 1)
  quicksort(arr, i + 1, hi)

print('\n# Quicksort')
nums = [10, 7, 2, 9, 1, 5]
print('Given array:', nums)
quicksort(nums)
print('Sorted:', nums)  # ==>
# Sorted [1, 2, 5, 7, 9, 10]


def quickselect(arr: List[int], k: int, lo: int = 0, hi: int = None):
  if hi is None: hi = len(arr) - 1
  if lo == hi: return arr[lo]

  pivot = arr[hi]
  i = lo
  for j in range(lo, hi):
    if arr[j] <= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1

  arr[i], arr[hi] = arr[hi], arr[i]
  if len(arr) - k == i:
      return arr[i]
  elif len(arr) - k < i:
      return quickselect(arr, k, lo, i - 1)
  else:
      return quickselect(arr, k, i + 1, hi)

print('\n# Quickselect')
arr = [10, 7, 2, 9, 1, 5]
print('Given array:', arr)
print('quickselect 1:', quickselect(arr, 1))  # ==>
# quickselect 1: 10
print('quickselect 2:', quickselect(arr, 2))  # ==>
# quickselect 2: 9
