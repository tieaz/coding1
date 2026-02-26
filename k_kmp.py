# Chapter K ⇒ KMP

from typing import *


def naive_search(s: str, p: str) -> List[int]:
  matches = []
  for i in range(len(s) - len(p) + 1):
    match = True
    for j in range(len(p)):
      if s[i + j] != p[j]:
        match = False
        break

    if match:
      matches.append(i)

  return matches

print('# Naive search')
s = 'ABABDABABCABAB'
p = 'ABABC'
print(f's: {s}, p: {p}, naive search: {naive_search(s, p)}')  # ==>
# s: ABABDABABCABAB, p: ABABC, naive search: [5]


def compute_lps(p: str) -> List[int]:
  m = len(p)
  lps = [0] * m
  # Length of previous longest prefix suffix
  length = 0
  i = 1
  while i < m:
    if p[i] == p[length]:
      length += 1
      lps[i] = length
      i += 1
    elif length != 0:
      length = lps[length - 1]
      # Don't increment `i`.
    else:
      lps[i] = 0
      i += 1

  return lps

print('\n# Compute LPS')
for s in [
  'ABABC',
  'ababab',
  'abczzzababc',
]:
  print(f'LPS for "{s}":', compute_lps(s))
  # LPS for "ABABC": [0, 0, 1, 2, 0]
  # LPS for "ababab": [0, 0, 1, 2, 3, 4]
  # LPS for "abczzzababc": [0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3]


def kmp_search(s: str, p: str) -> List[int]:
  if not p: return -1
  lps = compute_lps(p)
  s_ix = 0
  p_ix = 0
  matches = []
  while s_ix < len(s):
    if s[s_ix] == p[p_ix]:
      s_ix += 1
      p_ix += 1

    if p_ix == len(p):
      matches.append(s_ix - p_ix)
      p_ix = lps[-1]

    if s_ix < len(s) and s[s_ix] != p[p_ix]:
      if p_ix != 0:
        p_ix = lps[p_ix - 1]
      else:
        s_ix += 1

  return matches

print('\n# KMP search')
s = 'ABABDABABCABAB'
p = 'ABABC'
print(f's: {s}, p: {p}, KMP: {kmp_search(s, p)}')  # ==>
# s: ABABDABABCABAB, p: ABABC, KMP: [5]

s = 'AAAAAAAAAAAAAA'
p = 'AAAAA'
print(f's: {s}, p: {p}, KMP: {kmp_search(s, p)}')  # ==>
# s: AAAAAAAAAAAAAA, p: AAAAA, KMP: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def longest_happy_prefix(s: str) -> str:
  lps = compute_lps(s)
  return s[:lps[-1]]

print('\n# Longest happy prefix')
for s in [
  'SAVES',
  'ABABAB',
  'ABCDABC',
]:
  print(f'{s}: {longest_happy_prefix(s)}')  # ==>
  # SAVES: S
  # ABABAB: ABAB
  # ABCDABC: ABC
