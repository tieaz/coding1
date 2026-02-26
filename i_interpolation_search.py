# Chapter I ⇒ Interpolation Search

from typing import *


def binary_search(arr: List[int], target: int) -> int:
  lo = 0
  hi = len(arr) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      hi = mid - 1
    else:
      lo = mid + 1

  return -1

print('# Binary search')
arr = [1, 3, 5, 6, 9, 12, 14, 15]
print('Given array:', arr)
print('Search 0:', binary_search(arr, 0))
# Search 0: -1
print('Search 1:', binary_search(arr, 1))
# Search 1: 0
print('Search 2:', binary_search(arr, 2))
# Search 2: -1
print('Search 3:', binary_search(arr, 3))
# Search 3: 1
print('Search 8:', binary_search(arr, 8))
# Search 8: -1
print('Search 9:', binary_search(arr, 9))
# Search 9: 4
print('Search 21:', binary_search(arr, 21))
# Search 21: -1


def binary_insert(arr, target):
  lo = 0
  hi = len(arr) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      hi = mid - 1
    else:
      lo = mid + 1

  return max(0, lo)

import bisect

print('\n# Binary insert and bisect')
arr = [1, 3, 5, 6, 9, 12, 14, 15]
print(f'Insert 0: {binary_insert(arr, 0)} (vs. bisect_let: {bisect.bisect_left(arr, 0)}')
# Insert 0: 0 (vs. bisect_let: 0
print(f'Insert 2: {binary_insert(arr, 2)} (vs. bisect_let: {bisect.bisect_left(arr, 2)}')
# Insert 2: 1 (vs. bisect_let: 1
print(f'Insert 8: {binary_insert(arr, 8)} (vs. bisect_let: {bisect.bisect_left(arr, 8)}')
# Insert 8: 4 (vs. bisect_let: 4
print(f'Insert 21: {binary_insert(arr, 21)} (vs. bisect_let: {bisect.bisect_left(arr, 21)}')
# Insert 21: 8 (vs. bisect_let: 8


def interpolation_search(arr: List[int], target: int) -> int:
  lo = 0
  hi = len(arr) - 1
  while lo <= hi and target >= arr[lo] and target <= arr[hi]:
    fraction = (target - arr[lo]) / (arr[hi] - arr[lo])
    pos = lo + int((hi - lo) * fraction)
    if arr[pos] == target:
      return pos
    if arr[pos] < target:
      lo = pos + 1
    else:
      hi = pos - 1

  return -1

print('\n# Interpolation search')
data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
print('Given array:', data)
for target in range(50):
  try:
    check = data.index(target)
  except ValueError:
    check = -1
  search = interpolation_search(data, target)
  print(f'target: {target}; interp: {search} (vs. {check})')
  assert search == check
  # target: 0; interp: -1 (vs. -1)
  # target: 1; interp: -1 (vs. -1)
  # target: 2; interp: -1 (vs. -1)
  # target: 3; interp: -1 (vs. -1)
  # target: 4; interp: -1 (vs. -1)
  # target: 5; interp: -1 (vs. -1)
  # target: 6; interp: -1 (vs. -1)
  # target: 7; interp: -1 (vs. -1)
  # target: 8; interp: -1 (vs. -1)
  # target: 9; interp: -1 (vs. -1)
  # target: 10; interp: 0 (vs. 0)
  # target: 11; interp: -1 (vs. -1)
  # target: 12; interp: 1 (vs. 1)
  # target: 13; interp: 2 (vs. 2)
  # target: 14; interp: -1 (vs. -1)
  # target: 15; interp: -1 (vs. -1)
  # target: 16; interp: 3 (vs. 3)
  # target: 17; interp: -1 (vs. -1)
  # target: 18; interp: 4 (vs. 4)
  # target: 19; interp: 5 (vs. 5)
  # target: 20; interp: 6 (vs. 6)
  # target: 21; interp: 7 (vs. 7)
  # target: 22; interp: 8 (vs. 8)
  # target: 23; interp: 9 (vs. 9)
  # target: 24; interp: 10 (vs. 10)
  # target: 25; interp: -1 (vs. -1)
  # target: 26; interp: -1 (vs. -1)
  # target: 27; interp: -1 (vs. -1)
  # target: 28; interp: -1 (vs. -1)
  # target: 29; interp: -1 (vs. -1)
  # target: 30; interp: -1 (vs. -1)
  # target: 31; interp: -1 (vs. -1)
  # target: 32; interp: -1 (vs. -1)
  # target: 33; interp: 11 (vs. 11)
  # target: 34; interp: -1 (vs. -1)
  # target: 35; interp: 12 (vs. 12)
  # target: 36; interp: -1 (vs. -1)
  # target: 37; interp: -1 (vs. -1)
  # target: 38; interp: -1 (vs. -1)
  # target: 39; interp: -1 (vs. -1)
  # target: 40; interp: -1 (vs. -1)
  # target: 41; interp: -1 (vs. -1)
  # target: 42; interp: 13 (vs. 13)
  # target: 43; interp: -1 (vs. -1)
  # target: 44; interp: -1 (vs. -1)
  # target: 45; interp: -1 (vs. -1)
  # target: 46; interp: -1 (vs. -1)
  # target: 47; interp: 14 (vs. 14)
  # target: 48; interp: -1 (vs. -1)
  # target: 49; interp: -1 (vs. -1)
