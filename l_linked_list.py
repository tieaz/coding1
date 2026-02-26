# Chapter L ⇒ Linked List

from typing import *

class SLLNode(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class DLLNode(object):
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev


def print_ll(prefix, head):
  if not head:
    print(prefix + ' <None>')
    return

  ptr = head
  vals = []
  while ptr:
    vals.append(str(ptr.val))
    ptr = ptr.next

  print(prefix + ' ' + '->'.join(vals))


Node = SLLNode

def create_singly_linked_list(vals) -> SLLNode:
  if not vals: return None
  return SLLNode(
    vals[0],
    next=create_singly_linked_list(vals[1:]),
  )


def reverse_linked_list(head: Node) -> Node:
  ptr = head
  back = None
  while ptr:
    ptr_next = ptr.next
    ptr.next = back
    back = ptr
    ptr = ptr_next

  return back

print('# Reverse linked list')
head = create_singly_linked_list([1, 2, 4, 8])
print_ll('Forward: ', head)  # ==>
# Forward: 1->2->4->8
rev = reverse_linked_list(head)
print_ll('Reversed: ', rev)  # ==>
# Reversed: 8->4->2->1


def nth_node_from_end(head: Node, n: int) -> Node:
  back = reverse_linked_list(head)
  for i in range(n - 1):
    back = back.next

  return back

print('\n# Nth node from end')
head = create_singly_linked_list([1, 2, 4, 8])
print_ll('list:', head)
print('2nd node from end via reversing:', nth_node_from_end(head, 2).val)  # ==>
# 2nd node from end via reversing: 4


def nth_node_from_end(
  head: Node, n: int,
) -> Node:
  if not head: return None
  ptr1, ptr2 = head, head
  for i in range(n):
    if not ptr2: return None
    ptr2 = ptr2.next

  while ptr2:
    ptr1 = ptr1.next
    ptr2 = ptr2.next

  return ptr1

head = create_singly_linked_list([1, 2, 4, 8])
print('Via two pointers:', nth_node_from_end(head, 2).val)  # ==>
# Via two pointers: 4


def detect_cycle(head: Node) -> bool:
  if not head: return False
  slow = head
  fast = head.next
  while fast and fast.next:
    if fast is slow or fast.next is slow:
      return True

    slow = slow.next
    fast = fast.next.next

  return False


print('\n# Detect cycle')
head = create_singly_linked_list([1, 2, 4, 8])
print_ll('list:', head)
print('Has cycle:', detect_cycle(head))
# Has cycle: False
two = head.next
eight = two.next.next
eight.next = two
print('Has cycle:', detect_cycle(head))
# Has cycle: True



def linked_list_cycle_start(head: Node) -> Node:
  if not head: return None
  slow = head
  fast = head.next
  while fast and fast.next:
    if fast is slow or fast.next is slow:
      break

    slow = slow.next
    fast = fast.next.next

  if not fast or not fast.next: return None

  length = 1
  ptr = slow
  while ptr.next is not slow:
    length += 1
    ptr = ptr.next

  ptr2 = head
  for _ in range(length):
    ptr2 = ptr2.next

  ptr1 = head
  while True:
    if ptr1.next is ptr2.next:
      return ptr1.next

    ptr1 = ptr1.next
    ptr2 = ptr2.next

print('\n# Linked list cycle start')
head = create_singly_linked_list([1, 2, 4, 8])
start = linked_list_cycle_start(head)
print('Cycle start:', start)  # ==>
# Cycle start: None
two = head.next
eight = two.next.next
eight.next = two
start = linked_list_cycle_start(head)
print('Cycle start:', start.val)  # ==>
# Cycle start: 2


def find_length(head: None) -> int:
  if not head: return 0
  return 1 + find_length(head.next)

def is_palindrome(head: Node) -> bool:
  length = find_length(head)
  if length <= 1: return True

  # Find node before middle:
  mid = head
  for i in range(length // 2 - 1):
      mid = mid.next

  # Reverse from `mid`.
  head2 = mid.next
  mid.next = None
  back = reverse_linked_list(head2)

  # Compare both halves.
  ptr1, ptr2 = head, back
  while ptr1 and ptr2:
    if ptr1.val != ptr2.val: return False
    ptr1 = ptr1.next
    ptr2 = ptr2.next

  return True


print('\n# Is palindrome')
print('1,2,1:', is_palindrome(create_singly_linked_list([1, 2, 1])))
# 1,2,1: True
print('1,2,2,1:', is_palindrome(create_singly_linked_list([1, 2, 2, 1])))
# 1,2,2,1: True
print('1,2,3,2,1:', is_palindrome(create_singly_linked_list([1, 2, 3, 2, 1])))
# 1,2,3,2,1: True
print('1,2,3,3,1:', is_palindrome(create_singly_linked_list([1, 2, 3, 3, 1])))
# 1,2,3,3,1: False
print('1,2,3,1,3:', is_palindrome(create_singly_linked_list([1, 2, 3, 1, 3])))
# 1,2,3,1,3: False


class LinkedList(object):
  def push_front(self, val) -> any:
    pass

  def pop_front(self) -> any:
    pass

  def push_back(self, val) -> any:
    pass

  def pop_back(self) -> any:
    pass


class DLLNode(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

  def remove(self) -> object:
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
    return self

  def insert_before(self, node: object) -> object:
    self.prev = node.prev
    if self.prev:
      self.prev.next = self

    self.next = node
    node.prev = self
    return self

  def insert_after(self, node: object) -> object:
    self.next = node.next
    if self.next:
      self.next.prev = self

    self.prev = node
    node.next = self
    return self

Node = DLLNode


class LinkedList(object):
  def __init__(self):
    self.head = DLLNode(None)
    self.tail = DLLNode(None)
    self.head.next = self.tail
    self.tail.prev = self.head

  def push_front(self, val) -> any:
    return DLLNode(val).insert_after(self.head)

  def push_back(self, val) -> any:
    return DLLNode(val).insert_before(self.tail)

  @property
  def is_empty(self) -> bool:
    return self.head.next is self.tail

  def pop_front(self) -> any:
    if self.is_empty: return None
    return self.head.next.remove().val

  def pop_back(self) -> any:
    if self.is_empty: return None
    return self.tail.prev.remove().val


print('\n# Doubly linked list')
ll = LinkedList()
print_ll('List:', ll.head)
# List: None->None
ll.push_back(1)
print_ll('push_back(1):', ll.head)
# push_back(1): None->1->None
ll.push_back(2)
print_ll('push_back(2):', ll.head)
# push_back(2): None->1->2->None
ll.push_back(3)
print_ll('push_back(3):', ll.head)
# push_back(3): None->1->2->3->None
print_ll('List:', ll.head)
# List: None->1->2->3->None
print('Pop front:', ll.pop_front())
# Pop front: 1
print_ll('List:', ll.head)
# List: None->2->3->None
print('Pop back:', ll.pop_back())
# Pop back: 3
print_ll('List:', ll.head)
# List: None->2->None
print('Pop back:', ll.pop_back())
# Pop back: 2
print_ll('List:', ll.head)
# List: None->None
print('Pop front:', ll.pop_front())
# Pop front: None
