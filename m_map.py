# Chapter M ⇒ Map

from typing import *


class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

from collections import namedtuple
KV = namedtuple('KV', ['key', 'value'])


class Map(object):
  def __init__(self, n=4):
    self.n = n
    self.table = [None] * n

  def _get_node(self, key: str) -> Node:
    ix = hash(key) % self.n
    ptr = self.table[ix]
    # Traverse linked list looking for `key`.
    while ptr and ptr.val.key != key:
      ptr = ptr.next

    return ix, ptr

  def get(self, key: str) -> str:
    _, ptr = self._get_node(key)
    return ptr and ptr.val.value

  def put(self, key: str, value: str) -> None:
    ix, ptr = self._get_node(key)
    if ptr:
      # Replace the old value with the new.
      ptr.val = KV(key=key, value=value)
    else:
      # Insert new node at head of list.
      self.table[ix] = Node(
        KV(key=key, value=value),
        next=self.table[ix],
      )

  def remove(self, key: str) -> None:
    ix = hash(key) % self.n
    ptr = self.table[ix]
    if ptr and ptr.val.key == key:
      self.table[ix] = ptr.next
      return

    while ptr.next:
      if ptr.next.val.key == key:
          ptr.next = ptr.next.next
          return

      ptr = ptr.next

  def rebalance(self):
    new_map = Map(n=2 * self.n)
    for i in range(self.n):
      ptr = self.table[i]
      while ptr:
        new_map.put(ptr.val.key, ptr.val.value)
        ptr = ptr.next

    self.n = new_map.n
    self.table = new_map.table

print('\n# Design map/hashmap')
m = Map()
print("m.put('13', 'foo'):", m.put('13', 'foo'))
print("m.put('-3', 'zoo'):", m.put('-3', 'zoo'))
print("m.get('13'):", m.get('13')  )
print("m.get('-3'):", m.get('-3')  )
print("m.put('-2', 'bar'):", m.put('-2', 'bar'))
print("m.get('-2'):", m.get('-2')  )
print("m.remove('-3'):", m.remove('-3'))
print("m.get('-3'):", m.get('-3'))
print("m.get('0'):", m.get('0'))


m.rebalance()
print(m.n, m.table)
print("m.get('13'):", m.get('13'))
print("m.get('-3'):", m.get('-3'))
print("m.get('-2'):", m.get('-2'))
print("m.get('0'):", m.get('0'))


VN = namedtuple('VN', ['val', 'node'])


class DLLNode(object):
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

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


class LRUCache(object):
  def __init__(self, capacity):
    self.capacity = capacity
    self.map: Dict[any, VN] = {}
    self.list = LinkedList()

  def _push_front(self, key, value):
    node = self.list.push_front(key)
    self.map[key] = VN(val=value, node=node)
    return node

  def get(self, key) -> any:
    vn = self.map.get(key)
    # Move to the front of the linked list.
    vn.node.remove()
    self._push_front(key, vn.val)
    return vn.val

  def put(self, key, value):
    if key in self.map:
      vn = self.map[key]
      # Move to the front of linked list.
      vn.node.remove()
      self._push_front(key, value)
    else:
      if len(self.map) >= self.capacity:
        # Evict oldest entry.
        old_key = self.list.pop_back()
        del self.map[old_key]

      self._push_front(key, value)


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


print('\n# LRU cache')
cache = LRUCache(3)
print_ll(f'Cache keys and list: {cache.map.keys()};', cache.list.head)
# Cache keys and list: dict_keys([]); None->None
cache.put('A', 'ablob')
print('> get A:', cache.get('A'))
# > get A: ablob
print_ll(f'Cache keys and list: {cache.map.keys()};', cache.list.head)
# Cache keys and list: dict_keys(['A']); None->A->None
cache.put('B', 'bblob')
print('> get B:', cache.get('B'))
# > get B: bblob
print_ll(f'Cache keys and list: {cache.map.keys()};', cache.list.head)
# Cache keys and list: dict_keys(['A', 'B']); None->B->A->None
cache.put('C', 'cblob')
print('> get C:', cache.get('C'))
# > get C: cblob
print_ll(f'Cache keys and list: {cache.map.keys()};', cache.list.head)
# Cache keys and list: dict_keys(['A', 'B', 'C']); None->C->B->A->None
cache.put('A', 'ablobnew')
print_ll(f'After A->ablobnew: {cache.map.keys()};', cache.list.head)
# After A->ablobnew: dict_keys(['A', 'B', 'C']); None->A->C->B->None
cache.put('D', 'dblob')
print_ll(f'After D->dblob: {cache.map.keys()};', cache.list.head)
# After D->dblob: dict_keys(['A', 'C', 'D']); None->D->A->C->None
