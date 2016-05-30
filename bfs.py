"""
'bfs.py' implements the Breadth First Search algorithm.
"""

def bfs(src, sink):
  """
  Returns shortest path between 'src' and 'sink'.

  Arguments:
    src  <ConceptNode> : Source node (start).
    sink <ConceptNode> : Sink node (goal).

  Returns:
    <[ConceptNode,]> - list of concept nodes representing the path from 'src' to 'sink'
    in the cause-effect graph.
  """
  visited = set()
  queue = [[src]]
  while queue:
    path = queue.pop(0)
    if path[-1].concept == sink.concept:
      return path
    for effect in path[-1].effects:
      if effect not in visited:
        queue.append(path + [effect])
        visited.add(effect)

