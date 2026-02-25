# Chapter D ⇒ DP

from typing import *
import time

FIB_N = 10

def fib(n: int) -> int:
  if n <= 1: return n
  return fib(n - 1) + fib(n - 2)

start = time.perf_counter()
for i in range(FIB_N):
  print('fib', i, ':', fib(i))

print('Recursive fib:', time.perf_counter() - start)


def fib_dp(n: int) -> int:
  seq = [0, 1]
  for i in range(2, n + 1):
    seq.append(seq[i - 1] + seq[i - 2])

  return seq[n]

start = time.perf_counter()
for i in range(FIB_N):
  print('fib_dp', i, ':', fib_dp(i))

print('DP fib:', time.perf_counter() - start)


_CACHE: dict[int, int] = {}
def fib_cache(n: int) -> int:
  if n <= 1: return n
  global _CACHE
  if n not in _CACHE:
    value = fib_cache(n - 1) + fib_cache(n - 2)
    _CACHE[n] = value

  return _CACHE[n]


start = time.perf_counter()
for i in range(FIB_N):
  print('fib', i, ':', fib_cache(i))

print('Memoized fib:', time.perf_counter() - start)


import functools

@functools.cache
def fib_cache(n: int) -> int:
  if n <= 1: return n
  return fib_cache(n - 1) + fib_cache(n - 2)

print(fib_cache(100))


def palindromic_quadratic(s: str) -> str:
  if len(s) <= 1: return s
  max_substr = s[0]
  for i in range(len(s)):
    for j in range(i, len(s)):
      substr = s[i:j + 1]
      if (substr == substr[::-1] and
          len(substr) > len(max_substr)):
        max_substr = substr

  return max_substr


def palindromic_rec(s: str) -> str:
  if len(s) <= 1: return s

  if s[0] == s[-1]:
    inner_pal = palindromic_rec2(s[1:-1])
    if len(inner_pal) == len(s) - 2:
      return s

  return max([
    palindromic_rec2(s[1:]),
    palindromic_rec2(s[:-1]),
  ], key=len)


def palindromic_dp(s: str) -> str:
  n = len(s)
  if n <= 1: return s

  def check_core(i, size):
    j = i + size - 1
    max_substr = s[i:j + 1]
    offset = 1
    while (i - offset >= 0 and j + offset < n and
        s[i - offset] == s[j + offset]):
      max_substr = s[i - offset:j + offset + 1]
      offset += 1

    return max_substr

  return max(
    [check_core(i, 1) for i in range(n)] +
    [check_core(i, 2) for i in range(n - 1) if s[i] == s[i + 1]],
    key=len,
  )


def house_robber_arr(houses: List[int]) -> int:
  n = len(houses)
  dont_rob = [0] * n
  do_rob = [houses[0]] * n
  for i in range(1, n):
    do_rob[i] = houses[i] + dont_rob[i - 1]
    dont_rob[i] = max(dont_rob[i - 1], do_rob[i - 1])

  return max(do_rob[-1], dont_rob[-1])

print(house_robber_arr(houses))  # ==>
16


from collections import namedtuple

VI = namedtuple('VI', ['val', 'ixes'])
print(VI(val=3, ixes=[1]))  # ==>
VI(val=3, ixes=[1])
print(
  max(
    VI(val=1, ixes=[1]),
    VI(val=2, ixes=[]),
  ),
)  # ==>
VI(val=2, ixes=[])


def house_robber_which(houses: List[int]) -> int:
  do_rob = VI(val=houses[0], ixes=[0])
  dont_rob = VI(val=0, ixes=[])
  for i in range(1, len(houses)):
    do_rob, dont_rob = (
      VI(
        val=houses[i] + dont_rob.val,
        ixes=dont_rob.ixes + [i],
      ),
      max(do_rob, dont_rob),
    )

  return max(do_rob, dont_rob).ixes

print(house_robber_which(houses))  # ==>
[0, 2, 5]


def house_robber_circle(houses: List[int]) -> int:
  dont_rob0 = house_robber(houses[1:])
  do_rob0 = houses[0] + (
    house_robber(houses[2:-1]) if houses[2:-1] else 0
  )
  return max(dont_rob0, do_rob0)

print(house_robber([1,2,3]))
4
print(house_robber([1,2,3,4,5]))
9
print(house_robber_circle([1,2,3]))
3
print(house_robber_circle([1,2,3,4,5]))
8


class TreeNode:
  def __init__(
    self,
    val=0,
    left=None,
    right=None,
  ):
    self.val = val
    self.left = left
    self.right = right

rll = TreeNode(val=3)
rlr = TreeNode(val=7)
rl = TreeNode(val=4, left=rll, right=rlr)

rrr = TreeNode(val=8)
rr = TreeNode(val=5, right=rrr)

root = TreeNode(val=3, left=rl, right=rr)

DoDont = namedtuple('DoDont', ['do', 'dont'])

def house_robber_tree(root: TreeNode) -> int:
  def max_rob(node: TreeNode) -> DoDont:
    if not node: return DoDont(do=0, dont=0)

    max_left = max_rob(node.left)
    max_right = max_rob(node.right)

    return DoDont(
      do=node.val + max_left.dont + max_right.dont,
      dont=max(max_left) + max(max_right),
    )

  return max(max_rob(root))

print(house_robber_tree(root))
21
