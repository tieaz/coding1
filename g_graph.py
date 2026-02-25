# Chapter G ⇒ Graph

from typing import *

def graph_from_matrix(
  adj_matrix: List[List[int]],
) -> dict[str, set]:
  n = len(adj_matrix)
  node_id = lambda i: chr(ord('A') + i)
  graph = {}
  for i in range(n):
    graph[node_id(i)] = set([
      node_id(j)
      for j in range(n)
      if adj_matrix[i][j]
    ])

  return graph

adj_matrix = [
  [0, 1, 0, 0],
  [1, 0, 1, 1],
  [0, 1, 0, 0],
  [0, 1, 0, 0],
]
graph = graph_from_matrix(adj_matrix)
print(graph)  # ==>
{
  'A': {'B'},
  'B': {'C', 'A', 'D'},
  'C': {'B'},
  'D': {'B'},
}


def graph_from_list(
  adj_list: List[List[int]],
) -> dict[str, set]:
  n = len(adj_list)
  node_id = lambda i: chr(ord('A') + i)
  graph = {}
  for i in range(n):
    graph[node_id(i)] = set([
      node_id(j) for j in adj_list[i]
    ])

  return graph


adj_list = [
  [1],
  [0, 2, 3],
  [1],
  [1],
]
graph = graph_from_list(adj_list)
print(graph)  # ==>
{
  'A': {'B'},
  'B': {'C', 'A', 'D'},
  'C': {'B'},
  'D': {'B'},
}


import heapq

def dijkstra(
  graph: dict[str, dict[str, int]], start: str,
) -> dict[str, int]:
  dist = {node: float('inf') for node in graph}
  dist[start] = 0
  queue = [(0, start)]
  while queue:
    cur_dist, node = heapq.heappop(queue)
    if cur_dist > dist[node]:
      continue

    for neighbor, weight in graph[node].items():
      new_dist = cur_dist + weight
      if new_dist < dist[neighbor]:
        dist[neighbor] = new_dist
        heapq.heappush(queue, (new_dist, neighbor))

  return dist


from collections import namedtuple

DP = namedtuple('DP', ['dist', 'path'])
def dijkstra_path(
  graph: dict[str, dict[str, int]], start: str,
) -> dict[str, int]:
  dist = {node: DP(dist=float('inf'), path=[]) for node in graph}
  dist[start] = DP(dist=0, path=[start])
  queue = [dist[start]]
  while queue:
    cur_dist, path = heapq.heappop(queue)
    if cur_dist > dist[path[-1]].dist:
      continue

    for neighbor, weight in graph[path[-1]].items():
      new_dist = cur_dist + weight
      if new_dist < dist[neighbor].dist:
        dist[neighbor] = DP(
          dist=new_dist,
          path=path + [neighbor],
        )
        heapq.heappush(queue, dist[neighbor])

  return dist

flight_graph = graph_from_matrix([
  [  0, 100,   0,   0],
  [  0,   0, 100, 400],
  [ 50,   0,   0, 250],
  [  0,   0,   0,   0],
])
print('\nFLIGHT GRAPH!')
print(graph)
print(dijkstra(flight_graph, 'A'))
{
  'A': 0,
  'B': 100,
  'C': 200,
  'D': 450,
}
print(dijkstra_path(flight_graph, 'A'))
{
  'A': DP(dist=0, path=['A']),
  'B': DP(dist=100, path=['A', 'B']),
  'C': DP(dist=200, path=['A', 'B', 'C']),
  'D': DP(dist=450, path=['A', 'B', 'C', 'D']),
}


def course_schedule_dfs(
  num_courses: int, prereqs: List[List[int]],
) -> bool:
  graph = {i: [] for i in range(num_courses)}
  for a, b in prereqs:
    graph[b].append(a)

  for i in range(num_courses):
    visited = set()
    queue = [i]
    while queue:
      node = queue.pop(0)
      if node in visited:
        return False

      visited.add(node)
      queue.extend(graph[node])

  return True


def course_schedule(
  num_courses: int, prereqs: List[List[int]],
) -> bool:
  graph = {i: [] for i in range(num_courses)}
  for a, b in prereqs:
      graph[b].append(a)

  for i in range(num_courses):
      queue = [[i]]
      while queue:
          path = queue.pop(0)
          for j in graph[path[-1]]:
              if j in path:
                  return False
              queue.append(path + [j])

  return True

print('Simple:', course_schedule_dfs(3, [[1,0]]))
print('Simple:', course_schedule(3, [[1,0]]))

print('Bad:', course_schedule_dfs(3, [[1,0],[0,1],[2,1]]))
print('Bad:', course_schedule(3, [[1,0],[0,1],[2,1]]))

print('Diamond:', course_schedule_dfs(5, [[1,4],[2,4],[3,1],[3,2]]))
print('Diamond:', course_schedule(5, [[1,4],[2,4],[3,1],[3,2]]))


def bellman_ford(
  graph: dict[str, dict[str, int]], start: str
) -> dict[str, int]:
  dist = {node: float('inf') for node in graph}
  dist[start] = 0

  for count in range(len(graph) - 1):
    for node in graph:
      for neighbor, weight in graph[node].items():
        if dist[node] + weight < dist[neighbor]:
          dist[neighbor] = dist[node] + weight

  for node in graph:
    for neighbor, weight in graph[node].items():
      if dist[node] + weight < dist[neighbor]:
        raise ValueError('Negative cycle detected')

  return dist
