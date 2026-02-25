# Chapter H ⇒ Heap

from typing import *

from heapq import heapify,heappush,heappop,heappushpop
import random

arr =        [9, 7, 15, 12, 16, 2, 14, 8, 15, 16, 18, 6]
sorted_arr = [2, 6, 7, 8, 9, 12, 14, 15, 15, 16, 16, 18]
heap_arr =   [2, 7, 6, 8, 16, 9, 14, 12, 15, 16, 18, 15]


arr = [7, 9, 2, 3, 8, 5]
heapify(arr)
print(arr)
[2, 3, 5, 9, 8, 7]

print(heappop(arr))  # ==>
2
print(arr)  # ==>
[3, 7, 5, 9, 8]

heappush(arr, 2)
print(arr)  # ==>
[2, 7, 3, 9, 8, 5]

heappushpop(arr, 4)
print(arr)  # ==>
[3, 7, 4, 9, 8, 5]

print(heappop(arr))  # ==>
3
print(arr)


arr = [random.random() for _ in range(1000)]
k = 17

def kth_largest_element(arr: List[int], k: int) -> int:
  heap = arr[:k]
  heapify(heap)
  for i in range(k, len(arr)):
    if arr[i] > heap[0]:
      heappushpop(heap, arr[i])

  return heap[0]

print('k\'th largest:', kth_largest_element(arr, k))


def kth_smallest_element(arr: List[int], k: int) -> int:
  heap = [-x for x in arr[:k]]
  heapify(heap)
  for i in range(k, len(arr)):
    if arr[i] < -heap[0]:
      heappushpop(heap, -arr[i])

  return -heap[0]


def mergesort(arr: List[int]) -> List[int]:
  if len(arr) < 2: return arr
  n = len(arr)
  left = mergesort(arr[:n // 2])
  right = mergesort(arr[n // 2:])
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

arr = [random.randint(1, 100) for _ in range(100)]
sorted_arr = mergesort(arr)
print('arr:', arr)
print('sorted_arr:', sorted_arr)
assert sorted_arr == list(sorted(arr))


from collections import namedtuple

VI = namedtuple('VI', ['val', 'ix'])
def mergesort_kway(arrs: List[List[int]]) -> List[int]:
  k = len(arrs)
  ixes = [0] * k
  sorted_arr = []
  while True:
    lead_elems = [
      VI(val=arrs[i][ixes[i]], ix=i)
      for i in range(k) if ixes[i] < len(arrs[i])
    ]
    if not lead_elems:
      break

    lead_elems.sort()
    sorted_arr.append(lead_elems[0].val)
    ixes[lead_elems[0].ix] += 1

  return sorted_arr

print(mergesort_kway([[1,2,3], [0,4,6,8], [], [5,7,9]]))  # ==>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


VAI = namedtuple('VAI', ['val', 'arrs_ix', 'ix'])
def mergesort_kway_heap(arrs: List[List[int]]) -> List[int]:
  k = len(arrs)
  heap = [
    VAI(val=arrs[i][0], arrs_ix=i, ix=0)
    for i in range(k) if arrs[i]
  ]
  heapify(heap)
  sorted_arr = []
  while heap:
    lead_elem, arrs_ix, ix = heappop(heap)
    sorted_arr.append(lead_elem)
    if ix + 1 < len(arrs[arrs_ix]):
      heappush(
        heap,
        VAI(val=arrs[arrs_ix][ix + 1], arrs_ix=arrs_ix, ix=ix + 1),
      )

  return sorted_arr

print(mergesort_kway_heap([[1,2,3], [0,4,6,8], [], [5,7,9]]))  # ==>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



import bisect

class StreamingMedianSorted(object):
  def __init__(self):
    self.sorted = []

  def push(self, item: int) -> int:
    bisect.insort_left(self.sorted, item)
    return self.median

  @property
  def median(self):
    n = len(self.sorted)
    if n % 2 == 1:
      return self.sorted[n // 2]
    return 0.5 * (
      self.sorted[(n - 1) // 2] +
      self.sorted[(n - 1) // 2 + 1]
    )


class StreamingMedianMMM(object):
  def __init__(self):
    self.lo = []
    self.hi = []

  def push(self, item):
    heappush(self.hi, -heappushpop(self.lo, -item))
    if len(self.hi) > len(self.lo):
      heappush(self.lo, -heappop(self.hi))

    return self.median

  @property
  def median(self):
    if not self.lo:
      return 0
    if len(self.lo) > len(self.hi):
      return -self.lo[0]
    return 0.5 * (self.hi[0] - self.lo[0])

srt = StreamingMedianSorted()
mmm = StreamingMedianMMM()
for i in range(1, 20):
  print('\nSorted i:', i, '>', srt.push(i))
  print('MMM    i:', i, '>', mmm.push(i))
