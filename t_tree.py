# Chapter T ⇒ Tree

from typing import *


class TreeNode(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def build_preorder(arr: List[int]) -> TreeNode:
  if not arr: return None
  root = TreeNode(arr.pop(0))
  queue = [root]
  while queue and arr:
    node = queue.pop(0)
    left = arr.pop(0)
    right = arr.pop(0)
    if left is not None:
      node.left = TreeNode(left)
      queue.append(node.left)
    if right is not None:
      node.right = TreeNode(right)
      queue.append(node.right)

  return root


def print_tree(node: TreeNode):
  queue = [node]
  while queue:
    node = queue.pop(0)
    print(node.val, '-> left:', node.left and node.left.val, ', right:', node.right and node.right.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)

arr = [1, 2, 3, 4, 5, 6, 7]
print('Preorder:')
preorder_root = build_preorder(arr[:])
print_tree(preorder_root)

print('Postorder:')
postorder_root = build_postorder(arr[:])
print_tree(postorder_root)


def preorder_rec(node: TreeNode):
  if not node: return []
  return (
    [node.val] +
    preorder_rec(node.left) +
    preorder_rec(node.right)
  )

def inorder_rec(node: TreeNode):
  if not node: return []
  return (
    inorder_rec(node.left) +
    [node.val] +
    inorder_rec(node.right)
  )

def postorder_rec(node: TreeNode):
  if not node: return []
  return (
    postorder_rec(node.left) +
    postorder_rec(node.right) +
    [node.val]
  )


def level_order(root: TreeNode) -> List[int]:
  queue = [root]
  traversal = []
  while queue:
    node = queue.pop(0)
    traversal.append(node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)

  return traversal

level = level_order(preorder_root)
print('Level order:', level)
# Level order: [1, 2, 3, 4, 5, 6, 7]


def preorder(root: TreeNode) -> List[int]:
  stack = [root]
  traversal = []
  while stack:
    node = stack.pop()
    traversal.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)

  return traversal


def inorder(root: TreeNode) -> List[int]:
  stack = []
  node = root
  traversal = []

  while stack or node:
    # Put all leftmost children on stack.
    while node:
      stack.append(node)
      node = node.left

    node = stack.pop()
    traversal.append(node.val)
    node = node.right

  return traversal


def postorder(root: TreeNode) -> List[int]:
  stack = [root]
  traversal = []
  while stack:
    node = stack.pop()
    traversal.append(node.val)
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)

  return list(reversed(traversal))


def tree_depth(node: TreeNode, depth: int=0) -> int:
  if not node: return 0
  return max(
    depth,
    tree_depth(node.left, depth=depth + 1),
    tree_depth(node.right, depth=depth + 1),
  )


from collections import namedtuple

NV = namedtuple('NV', ['node', 'val'])
def max_depth(root: TreeNode) -> List[int]:
  stack = [NV(node=root, val=0)]
  max_depth = 0
  while stack:
    node, depth = stack.pop()
    max_depth = max(max_depth, depth)
    if node.right:
      stack.append(NV(node=node.right, val=depth + 1))
    if node.left:
      stack.append(NV(node=node.left, val=depth + 1))

  return max_depth


print(max_depth(root))  # ==>
2


def is_full(node: TreeNode) -> bool:
  if not node: return True
  if (node.left is None) ^ (node.right is None):
    return False
  return (
    is_full(node.left) and
    is_full(node.right)
  )


def is_balanced(root: TreeNode) -> bool:
  if not root: return True
  stack = [NV(node=root, val=0)]
  leaf_depths = set()
  while stack:
    node, depth = stack.pop()
    if not node.left and not node.right:
      leaf_depths.add(depth)
    else:
      if node.left:
        stack.append(NV(node=node.left, val=depth + 1))
      if node.right:
        stack.append(NV(node=node.right, val=depth + 1))

  return max(leaf_depths) - min(leaf_depths) <= 1


def is_complete(root: TreeNode) -> bool:
  if not root: return True
  stack = [NV(node=root, val=0)]
  depth_counts = defaultdict(int)
  while stack:
    node, depth = stack.pop()
    depth_counts[depth] += 1
    if node.left:
      stack.append(NV(node=node.left, val=depth + 1))
    if node.right:
      stack.append(NV(node=node.right, val=depth + 1))

  for depth in range(0, max(depth_counts.keys())):
    if depth_counts[depth] != pow(2, depth):
      return False

  return True


for arr in [
  [],
  [1],
  [1,2,None],
  [1,2,3],
  [1,2,3,4,5,6,7],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,None,None,6,7,8,9,10,11],
]:
  node = build_preorder(arr[:])
  print('\nTree:', arr)
  print('depth:', tree_depth(node))
  print('is_full:', is_full(node))
  print('is_balanced:', is_balanced(node))
  print('is_complete:', is_complete(node))


def lowest_common_ancestor(node, p, q):
  if node is None or node is p or node is q:
    return node

  left = lowest_common_ancestor(node.left, p, q)
  right = lowest_common_ancestor(node.right, p, q)
  if left and right:
    return node
  return left if left else right

ll = TreeNode(3)
lr = TreeNode(4)
l = TreeNode(1, left=ll, right=lr)
r = TreeNode(2)
root = TreeNode(0, left=l, right=r)

print(lowest_common_ancestor(root, ll, lr).val)  # ==>
1


def is_valid_bst(root: TreeNode) -> bool:
  def check_node(
    node: Optional[TreeNode],
    lower: Optional[int],
    upper: Optional[int],
  ) -> bool:
    if not node: return True
    if lower is not None and node.val < lower:
      return False
    if upper is not None and node.val >= upper:
      return False

    return (
      check_node(node.left, lower, node.val) and
      check_node(node.right, node.val, upper)
    )

  return check_node(root, None, None)


print('is_valid_bst:', is_valid_bst(bst_root))
# is_valid_bst: True
print('is_valid_bst (imbalanced):', is_valid_bst(build_preorder([25, 20, 36, 10, 22, 30, 20])))
# is_valid_bst (imbalanced): False
print('is_valid_bst (imbalanced):', is_valid_bst(build_preorder([25, 20, 36, 30, 22, 30, 40])))
# is_valid_bst (imbalanced): False
