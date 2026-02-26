# Chapter Z ⇒ Z-Algorithm

from typing import *


def naive_z_algorithm(s: str) -> List[int]:
  n = len(s)
  z = [0] * n
  z[0] = n
  for i in range(1, n):
    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
      z[i] += 1

  return z

print('# Naive Z-algorithm')
s = 'aabcaabxaaz'
print(f'{s}: {naive_z_algorithm(s)}')  # ==>
# aabcaabxaaz: [11, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]


def z_algorithm_box(s: str) -> List[int]:
  n = len(s)
  z = [0] * n
  z[0] = n
  left, right = 0, 0
  for i in range(1, n):
    if i <= right and i + z[i - left] <= right:
      z[i] = z[i - left]
    else:
      left = i
      if i > right: right = i
      while right < n and s[right - left] == s[right]:
        right += 1

      z[i] = right - left
      right -= 1

  return z

print('\n# Z-algorithm box')
s = 'aabcaabxaaz'
print(f'{s}: {z_algorithm_box(s)}')
# aabcaabxaaz: [11, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]


def pattern_matching_z(s, p):
  concat = p + '$' + s
  n = len(concat)
  m = len(p)
  z = z_algorithm_box(concat)

  matches = []
  for i in range(m + 1, n):  # Skip pattern and separator
    if z[i] == m:
      matches.append(i - m - 1)

  return matches

print('\n# Pattern matching')
s='ABABDABABCABAB'
p='ABABC'
print(f's: {s}, p: {p}, matching with Z-algorithm: {pattern_matching_z(s, p)}')  # ==>
# s: ABABDABABCABAB, p: ABABC, matching with Z-algorithm: [5]


def repeated_substring(s: str) -> str:
  n = len(s)
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      substr = s[:i]
      if s == substr * (n // i):
        return substr

  return s

print('\n# Repeated substring')
for s in [
  'aaaaa',
  'abcdefg',
  'abcabcabcabc',
  'xyxy',
  'xyxyxy',
]:
  print(f'Naive for "{s}": {repeated_substring(s)}')  # ==>
  # Naive for "aaaaa": a
  # Naive for "abcdefg": abcdefg
  # Naive for "abcabcabcabc": abc
  # Naive for "xyxy": xy
  # Naive for "xyxyxy": xy


def repeated_substring_z(s: str) -> str:
  z = z_algorithm_box(s)
  n = len(s)
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      j = i
      while j < n and z[j] >= i:
        j += i

      if j >= n:
        return s[:i]

  return s

for s in [
  'aaaaa',
  'abcdefg',
  'abcabcabcabc',
  'xyxy',
  'xyxyxy',
]:
  print(f'Z-algorithm for "{s}": {repeated_substring_z(s)}')  # ==>
  # Z-algorithm for "aaaaa": a
  # Z-algorithm for "abcdefg": abcdefg
  # Z-algorithm for "abcabcabcabc": abc
  # Z-algorithm for "xyxy": xy
  # Z-algorithm for "xyxyxy": xy


def shortest_palindrome_len(s: str) -> str:
  concat = s + '$' + s[::-1]
  n = len(concat)
  z = z_algorithm_box(concat)

  for i in range(len(s) + 1, n):
    if i + z[i] == n:
      return len(s) - z[i]


def shortest_palindrome(s: str) -> str:
  concat = s + '$' + s[::-1]
  n = len(concat)
  z = z_algorithm_box(concat)

  for i in range(len(s) + 1, n):
    if i + z[i] == n:
      return s[z[i]:][::-1] + s

print('\n# Shortest palindrome')
for s in [
  'wxyz',
  'aaa',
  'abaaa',
]:
  print(f'Length for "{s}": {shortest_palindrome_len(s)}, and actual palindrome: {shortest_palindrome(s)}')  # ==>
  # Length for "wxyz": 3, and actual palindrome: zyxwxyz
  # Length for "aaa": 0, and actual palindrome: aaa
  # Length for "abaaa": 2, and actual palindrome: aaabaaa
