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

arr = [1, 3, 5, 6, 9, 12, 14, 15]
print('Insert 0', binary_insert(arr, 0), bisect.bisect_left(arr, 0))
print('Insert 2', binary_insert(arr, 2), bisect.bisect_left(arr, 2))
print('Insert 8', binary_insert(arr, 8), bisect.bisect_left(arr, 8))
print('Insert 21', binary_insert(arr, 21), bisect.bisect_left(arr, 21))


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

data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
for target in range(50):
  try:
    check = data.index(target)
  except ValueError:
    check = -1
  search = interpolation_search(data, target)
  print('target:', target, search, check)
  assert search == check
