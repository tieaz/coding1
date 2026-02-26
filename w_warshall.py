# Chapter W ⇒ Warshall

from typing import *


def floyd_warshall(graph: dict) -> List[List[int]]:
  n = len(graph)
  dist = [[float('inf')] * n for i in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j:
        dist[i][j] = 0
      elif j in graph[i]:
        dist[i][j] = graph[i][j]

    for k in range(n):
      for i in range(n):
        for j in range(n):
          if dist[i][k] + dist[k][j] < dist[i][j]:
            dist[i][j] = dist[i][k] + dist[k][j]

  return dist

graph = {
  0: {1: 13, 2: 16},
  1: {0: 13, 2: 23, 3: 18},
  2: {0: 16, 1: 23, 3: 27, 4: 3},
  3: {1: 18, 2: 27},
  4: {2: 3},
}
print('Graph:', graph)
print('Floyd-Warshall on graph:', floyd_warshall(graph))
# Floyd-Warshall on graph: [
#   [0, 13, 16, 31, 19],
#   [13, 0, 23, 18, 26],
#   [16, 23, 0, 27, 3],
#   [31, 18, 27, 0, 30],
#   [19, 26, 3, 30, 0],
# ]



def most_remote_city(graph: dict) -> int:
  dist = floyd_warshall(graph)
  most_remote = None
  min_neighbors = None
  for i in range(len(dist)):
    neighbors_i = sum(1 for d in dist[i] if 0 < d <= 20)
    if most_remote is None or neighbors_i < min_neighbors:
      most_remote = i
      min_neighbors = neighbors_i

  return most_remote

print('\n# Most remote city')
print('On graph:', most_remote_city(graph))  # ==>
# On graph: 3


from collections import namedtuple

ND = namedtuple('ND', ['node', 'dist'])
def floyd_warshall_path(graph: dict) -> List[List[ND]]:
  n = len(graph)
  dist = [
    [ND(node=None, dist=float('inf'))] * n
    for i in range(n)
  ]
  for i in range(n):
    for j in range(n):
      if i == j:
        dist[i][j] = ND(node=i, dist=0)
      elif j in graph[i]:
        dist[i][j] = ND(node=j, dist=graph[i][j])

    for k in range(n):
      for i in range(n):
        for j in range(n):
          if dist[i][k].dist + dist[k][j].dist < dist[i][j].dist:
            dist[i][j] = ND(
              node=dist[i][k].node,
              dist=dist[i][k].dist + dist[k][j].dist,
            )

  return dist

print('\n# Floyd-Warshall with path')
print(floyd_warshall_path(graph))  # ==>
# [
#   [ND(0, 0), ND(1, 13), ND(2, 16), ND(1, 31), ND(2, 19)],
#   [ND(0, 13), ND(1, 0), ND(2, 23), ND(3, 18), ND(2, 26)],
#   [ND(0, 16), ND(1, 23), ND(2, 0), ND(3, 27), ND(4, 3)],
#   [ND(1, 31), ND(1, 18), ND(2, 27), ND(3, 0), ND(2, 30)],
#   [ND(2, 19), ND(2, 26), ND(2, 3), ND(2, 30), ND(4, 0)],
# ]


def graph_from_matrix_weighted(
  adj_matrix: List[List[int]],
) -> dict[str, set]:
  n = len(adj_matrix)
  node_id = lambda i: chr(ord('A') + i)
  graph = {}
  for i in range(n):
    graph[node_id(i)] = {
      node_id(j): adj_matrix[i][j]
      for j in range(n)
      if adj_matrix[i][j]
    }

  return graph


CIJ = namedtuple('CIJ', ['cost', 'i', 'j'])
def prims_algorithm(graph: object):
  cheapest = {i: CIJ(cost=float('inf'), i=i, j=None) for i in graph}

  nodes = list(graph.keys())
  explored = set()
  unexplored = set(nodes)

  cheapest[nodes[0]] = CIJ(cost=0, i=nodes[0], j=None)

  while unexplored:
    node = min(unexplored, key=lambda v: cheapest[v].cost)
    unexplored.remove(node)
    explored.add(node)
    for neighbor, weight in graph[node].items():
      if (neighbor in unexplored and
          weight < cheapest[neighbor].cost):
        cheapest[neighbor] = CIJ(cost=weight, i=node, j=neighbor)

    print(f'After exploring {node}:', ','.join(
      f'{i}-{j}'
      for cost, i, j in cheapest.values()
      if j is not None
    ))
    # After exploring A: A-B,A-D,A-E
    # After exploring B: A-B,B-C,A-D,A-E,B-F
    # After exploring C: A-B,B-C,C-D,A-E,C-F,C-G
    # After exploring D: A-B,B-C,C-D,A-E,C-F,C-G
    # After exploring F: A-B,B-C,C-D,F-E,C-F,F-G,F-H,F-J
    # After exploring G: A-B,B-C,C-D,F-E,C-F,F-G,G-H,G-I,F-J
    # After exploring I: A-B,B-C,C-D,F-E,C-F,F-G,I-H,G-I,I-J
    # After exploring H: A-B,B-C,C-D,F-E,C-F,F-G,I-H,G-I,H-J
    # After exploring J: A-B,B-C,C-D,F-E,C-F,F-G,I-H,G-I,H-J
    # After exploring E: A-B,B-C,C-D,F-E,C-F,F-G,I-H,G-I,H-J

  return [(i, j) for cost, i, j in cheapest.values() if j is not None]

print("\n# Prim's algorithm")
adj_matrix = [
  [0, 3, 0, 6,  9,  0, 0, 0, 0,  0],
  [3, 0, 2, 0,  9,  9, 0, 0, 0,  0],
  [0, 2, 0, 2,  0,  8, 9, 0, 0,  0],
  [6, 0, 2, 0,  0,  0, 9, 0, 0,  0],
  [9, 9, 0, 0,  0,  8, 0, 0, 0, 18],
  [0, 9, 8, 0,  8,  0, 7, 9, 0, 10],
  [0, 0, 9, 9,  0,  7, 0, 5, 4,  0],
  [0, 0, 0, 0,  0,  9, 5, 0, 1,  3],
  [0, 0, 0, 0,  0,  0, 4, 1, 0,  4],
  [0, 0, 0, 0, 18, 10, 0, 3, 4,  0],
]
graph = graph_from_matrix_weighted(adj_matrix)
print('From graph:', graph)
print('MST:', prims_algorithm(graph))  # ==>
# MST: [
#   ('A', 'B'),
#   ('B', 'C'),
#   ('C', 'D'),
#   ('F', 'E'),
#   ('C', 'F'),
#   ('F', 'G'),
#   ('I', 'H'),
#   ('G', 'I'),
#   ('H', 'J'),
# ]
