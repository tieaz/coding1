# Chapter O ⇒ O(•)

from typing import *


# Accessing fixed elements.
front = x[0]
back = x[-1]

# Accessing a random element.
import random
element = x[int(len(x) * random.random())]


def binary_search(arr, target):
  lo = 0
  hi = len(arr) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      lo = mid + 1
    else:
      hi = mid - 1
  return - 1


def search(arr, target, lo, hi):
  if lo > hi: return -1
  mid = (lo + hi) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] < target:
    return search(
      arr, target, mid + 1, hi)
  else:
    return search(
      arr, target, lo, mid - 1)


def fib(n: int) -> int:
  if n <= 1: return n
  return fib(n - 1) + fib(n - 2)


def permutations(arr):
  perms = []

  def inner(sub_arr, perm):
    if not sub_arr:
      perms.append(perm)
      return

    for i in range(len(sub_arr)):
      inner(
        sub_arr[:i] + sub_arr[i+1:],
        perm + [sub_arr[i]],
      )

  inner(arr, [])
  return perms

print(permutations([1,2,3]))  # ==>
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
