# Chapter X ⇒ XOR

from typing import *


def single_number_map(nums):
  counts = {}
  for n in nums:
    if n in counts:
      counts[n] += 1
    else:
      counts[n] = 1

  for key, value in counts.items():
    if value == 1:
      return key

print('# Find unique number')
arr = [1,2,3,4,1,2,5,5,4]
print('Given array:', arr)
print('With map:', single_number_map(arr))
# With map: 3


def single_number_sort(nums):
  nums.sort()
  ix = 0
  while ix < len(nums):
    if (ix + 1 < len(nums) and
        nums[ix] == nums[ix + 1]):
      ix += 2
    else:
      break

  return nums[ix]

print('With sorting:', single_number_sort(arr))
# With sorting: 3


def single_number(nums):
  xor = 0
  for n in nums:
    xor ^= n

  return xor

print('With xor:', single_number(arr))
# With xor: 3


def two_single_numbers(nums):
  x = 0
  for n in nums:
    x ^= n

  difference = x & -n

  bit_set = 0
  bit_unset = 0
  for n in nums:
    if n & difference == 0:
      bit_unset ^= n
    else:
      bit_set ^= n

  return [bit_set, bit_unset]

print('\n# Two single numbers')
arr = [1,2,3,4,1,2,6,5,4,5]
print('Given array:', arr)
print('With xor:', two_single_numbers(arr))


max_num = 50_000
# Use this for full demonstration (slow, takes 2–3 minutes).
# max_num = 500_000_000
f = 0.0
g = 0.0
for i in range(max_num + 1):
  if not i % 1_000_000: print(f'{i // 1_000_000}/{max_num // 1_000_000} ...')
  f += 1.0 * i
  g += 1.0 * (3001 if i == 3000 else i)

print('max_num:', max_num)
print('f:', f)
print('g:', g)
print('f == g:', f == g)
print('Closed form:', 1.0 * max_num * (max_num + 1) / 2)
# max_num: 500000000
# f: 1.250000000671089e+17
# g: 1.250000000671089e+17
# f == g: True
# Closed form: 1.2500000025e+17


def corrupted_latin_square_checksum(square):
  n = len(square)
  row_checksums = [0] * n
  col_checksums = [0] * n

  for r in range(n):
    for c in range(n):
      row_checksums[r] += square[r][c]
      col_checksums[c] += square[r][c]

  checksum = n * (n + 1) / 2
  r = [i for i in range(n) if row_checksums[i] != checksum][0]
  c = [i for i in range(n) if col_checksums[i] != checksum][0]
  return (r, c)

print('\n# Corrupted Latin square')
square = [
  [1,2,3,4,5],
  [2,3,5,1,4],
  [3,5,4,2,1],
  [4,1,2,1,3],  # [4,1,2,5,3],
  [5,4,1,3,2],
]
print('With square:')
print(square)
print('With checksum:', corrupted_latin_square_checksum(square))
# With checksum: (3, 3)


def corrupted_latin_square_xor(square):
  n = len(square)
  row_checksums = [0] * n
  col_checksums = [0] * n

  checksum = 0
  for r in range(n):
    checksum ^= (r + 1)
    for c in range(n):
      row_checksums[r] ^= square[r][c]
      col_checksums[c] ^= square[r][c]

  r = [i for i in range(n) if row_checksums[i] != checksum][0]
  c = [i for i in range(n) if col_checksums[i] != checksum][0]
  return (r, c)

print('With xor:', corrupted_latin_square_xor(square))
# With xor: (3, 3)
