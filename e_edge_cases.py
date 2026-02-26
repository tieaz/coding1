# Chapter E ⇒ Edge Cases

from typing import *


rr, cc = 0, 0
m, n = 10, 8
if not (0 <= rr < m and 0 <= cc < n):
  pass

if not (0 <= rr < m) or not (0 <= cc < n):
  pass

if not (0 <= rr and rr < m) or not (0 <= cc and cc < n):
  pass

if not 0 <= rr or not rr < m or not 0 <= cc or not cc < n:
  pass

if rr < 0 or rr >= m or cc < 0 or cc >= n:
  pass


graph = {
  0: [1, 2],
  1: [0],
  2: [0, 4],
  3: [4, 8],
  4: [2, 3, 5],
  5: [4, 9],
  6: [7, 10],
  7: [6, 11],
  8: [3],
  9: [5],
  10: [6, 11],
  11: [7, 10, 12],
  12: [11],
}


def union_find(graph: dict):
  n = len(graph)
  parents = [i for i in range(n)]

  def find(i: int):
    if parents[i] == i: return i
    return find(parents[i])

  def union(i: int, j: int):
    pi = find(i)
    pj = find(j)
    parent = min(pi, pj)
    parents[pi], parents[pj] = parent, parent

  print('> Starting parents:', parents)
  for i, edges in graph.items():
    for j in edges:
      union(i, j)
      print(f'> union({i}, {j}) -> parents:', parents)

  return len(set(find(i) for i in range(n)))

print('# Union find')
print('Number of islands:', union_find(graph))
# > Starting parents: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# > union(0, 1) -> parents: [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# > union(0, 2) -> parents: [0, 0, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# > union(1, 0) -> parents: [0, 0, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# > union(2, 0) -> parents: [0, 0, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# > union(2, 4) -> parents: [0, 0, 0, 3, 0, 5, 6, 7, 8, 9, 10, 11, 12]
# > union(3, 4) -> parents: [0, 0, 0, 0, 0, 5, 6, 7, 8, 9, 10, 11, 12]
# > union(3, 8) -> parents: [0, 0, 0, 0, 0, 5, 6, 7, 0, 9, 10, 11, 12]
# > union(4, 2) -> parents: [0, 0, 0, 0, 0, 5, 6, 7, 0, 9, 10, 11, 12]
# > union(4, 3) -> parents: [0, 0, 0, 0, 0, 5, 6, 7, 0, 9, 10, 11, 12]
# > union(4, 5) -> parents: [0, 0, 0, 0, 0, 0, 6, 7, 0, 9, 10, 11, 12]
# > union(5, 4) -> parents: [0, 0, 0, 0, 0, 0, 6, 7, 0, 9, 10, 11, 12]
# > union(5, 9) -> parents: [0, 0, 0, 0, 0, 0, 6, 7, 0, 0, 10, 11, 12]
# > union(6, 7) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 10, 11, 12]
# > union(6, 10) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 11, 12]
# > union(7, 6) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 11, 12]
# > union(7, 11) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 12]
# > union(8, 3) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 12]
# > union(9, 5) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 12]
# > union(10, 6) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 12]
# > union(10, 11) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 12]
# > union(11, 7) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 12]
# > union(11, 10) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 12]
# > union(11, 12) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 6]
# > union(12, 11) -> parents: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 6, 6, 6]
# Number of islands: 2


class Trie(object):
  def __init__(self, words: list[str]):
    self.root = {}
    self.end_symbol = "*"
    for word in words:
      self.insert(word)

  def insert(self, word: str) -> None:
    node = self.root
    for char in word:
      if char not in node:
        node[char] = {}
      node = node[char]
    node[self.end_symbol] = True

  def is_prefix(self, prefix: str) -> bool:
    node = self.root
    for char in prefix:
      if char not in node:
        return False
      node = node[char]
    return True

  def is_word(self, s: str) -> bool:
    node = self.root
    for char in s:
      if char not in node:
        return False
      node = node[char]
    return self.end_symbol in node

print('\n# Trie')
trie = Trie(['bee', 'bed', 'beg', 'add', 'act'])
print('Trie root:', trie.root)  # ==>
# Trie root: {
#   'b': {
#     'e': {
#       'e': {'*': True},
#       'd': {'*': True},
#       'g': {'*': True},
#     },
#   },
#   'a': {
#     'd': {
#       'd': {'*': True},
#     },
#     'c': {
#       't': {'*': True},
#     },
#   },
# }

print('is_prefix("ce"):', trie.is_prefix('ce'))  # ==>
# is_prefix("ce"): False
print('is_prefix("ad"):', trie.is_prefix('ad'))  # ==>
# is_prefix("ad"): True
print('is_word("bed"):', trie.is_word('bed'))  # ==>
# is_word("bed"): True
