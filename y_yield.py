# Chapter Y ⇒ yield

from typing import *
from collections import namedtuple


N = 5
# N = 100_000
# N = 1_000_000


def fib(n: int) -> List[int]:
  seq = [0, 1]
  for i in range(2, n + 1):
    print(f'> Calculating seq[{i}]')
    seq.append(seq[-1] + seq[-2])

  return seq

sign = 1
total = 0
for val in fib(N):
  print(f'Got fib({val})')
  total += sign * val
  sign *= -1

print('[list] Got sequence:', total)  # ==>
# > Calculating seq[2]
# > Calculating seq[3]
# > Calculating seq[4]
# > Calculating seq[5]
# Got fib(0)
# Got fib(1)
# Got fib(1)
# Got fib(2)
# Got fib(3)
# Got fib(5)
# [list] Got sequence: -4


def fib_yield(n: int) -> Iterator[int]:
  a, b = 0, 1
  yield a
  yield b
  for i in range(2, n + 1):
    print(f'> Calculating term {i}')
    a, b = b, a + b
    yield b

sign = 1
total = 0
for val in fib_yield(N):
  print(f'Got fib({val})')
  total += sign * val
  sign *= -1

print('[yield] Got sequence:', total)  # ==>
# Got fib(0)
# Got fib(1)
# > Calculating term 2
# Got fib(1)
# > Calculating term 3
# Got fib(2)
# > Calculating term 4
# Got fib(3)
# > Calculating term 5
# Got fib(5)
# [yield] Got sequence: -4


print('\n# namedtuples')
RMP = namedtuple('MP', ['remaining', 'matched', 'pattern'])

matcher = RMP(remaining='baaaaaa', matched='', pattern='ba*b')
print('.remaining:', matcher.remaining)  # ==>
# .remaining: baaaaaa
print('.matched:', matcher.matched)  # ==>
# .matched:
print('.pattern:', matcher.pattern)  # ==>
# .pattern: ba*b


import functools
import time

@functools.cache
def min_change(amount: int, coins: tuple[int]) -> int:
  if amount == 0: return 0

  min_coins = None
  for coin in coins:
    if coin > amount:
      continue

    sub_change = min_change(amount - coin, coins)
    if sub_change == -1:
      continue

    if min_coins is None:
      min_coins = sub_change
    else:
      min_coins = min(min_coins, sub_change)

  return 1 + min_coins if min_coins is not None else -1

print('\n# Minimum change')
start = time.perf_counter()
print('min_change(68):', min_change(68, (1, 5, 10, 25)))
# min_change(68): 7
print('Elapsed time:', time.perf_counter() - start)
# Elapsed time: 0.00019707599999999742
