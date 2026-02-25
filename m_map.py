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


cache = LRUCache(3)
print('Cache keys and list:', cache.map.keys(), ';', list2str(cache.list.head))
# Cache keys and list: dict_keys([]) ; None->None
cache.put('A', 'ablob')
# > get A: ablob
print('> get A:', cache.get('A'))
# Cache keys and list: dict_keys(['A']) ; None->A->None
print('Cache keys and list:', cache.map.keys(), ';', list2str(cache.list.head))
# Cache keys and list: dict_keys(['A', 'B']) ; None->B->A->None
cache.put('B', 'bblob')
# Cache keys and list: dict_keys(['A', 'B', 'C']) ; None->C->B->A->None
print('> get B:', cache.get('B'))
# > get B: bblob
cache.put('C', 'cblob')
print('> get C:', cache.get('C'))
# > get C: cblob
print('Cache keys and list:', cache.map.keys(), ';', list2str(cache.list.head))
print('Cache keys and list:', cache.map.keys(), ';', list2str(cache.list.head))
cache.put('A', 'ablobnew')
print('Cache keys and list:', cache.map.keys(), ';', list2str(cache.list.head))
# Cache keys and list: dict_keys(['A', 'B', 'C']) ; None->A->C->B->None
cache.put('D', 'dblob')
print('Cache keys and list:', cache.map.keys(), ';', list2str(cache.list.head))
# Cache keys and list: dict_keys(['A', 'C', 'D']) ; None->D->A->C->None
