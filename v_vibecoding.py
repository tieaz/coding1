# Chapter V ⇒ Vibecoding

from typing import *


class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


def has_cycle(head: Node) -> bool:
  visited = set()
  current = head
  while current:
    if current in visited:
      return True
    visited.add(current)
    current = current.next

  return False
  
print('# Cycle detection')
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print('Without cycle:', has_cycle(head))
# Without cycle: False
head.next.next.next = head
print('With cycle:', has_cycle(head))
# With cycle: True


def has_cycle(head: Node) -> bool:
  if not head: return False
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True

  return False


# > Naive prompt: 'Find if a target exists in an array'

# AI might give linear search O(n).
def find_target(arr, target):
  return target in arr

# > Constraint-first prompt: 'Find if a target exists in a sorted array.'

# AI immediately recognizes binary search is required:
def find_target(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return False
