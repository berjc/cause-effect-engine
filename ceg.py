"""
'ceg.py' implements the CEGraph class.
"""

from bfs          import bfs
from concept_node import ConceptNode

class CEGraph:
  """
  Implements a Cause-Effect graph.

  Attribute:
    nodes <{str:ConceptNode,}> : Map of concept to concept node in graph.
  """

  def __init__(self):
    """
    Initializes CEGraph.
    """
    self.nodes = {}

  def get_node(self, concept):
    """
    Returns concept node for concept from dict or creates  and returns concept node
    if non-existent.

    Argument:
      concept <str> : Description of concept.

    Returns:
      <ConceptNode> - concept node corresponding to 'concept' in graph
    """
    if concept not in self.nodes:
      concept_node = ConceptNode(concept)
      self.nodes[concept] = concept_node
    return self.nodes[concept]

  def add(self, cause, effect):
    """
    Adds cause and effect pair to graph.

    Arguments:
      cause  <str> : Description of cause concept.
      effect <str> : Description of effect concept.

    Returns:
      <(bool, str|NoneType)> - first item denotes whether an error occurred or not,
      the second item corresponds to an error message or 'None' if no error occurred.
    """
    cause_node = self.get_node(cause)
    effect_node = self.get_node(effect)
    if cause_node in effect_node.causes and effect_node in cause_node.effects:
      return (False, 'Cause \'%s\' and Effect \'%s\' already in Cause-Effect Graph.' \
        % (cause, effect))
    cause_node.add_effect(effect_node)
    effect_node.add_cause(cause_node)
    return (True, None)

  def resolve(self, src, sink):
    """
    Returns path from 'src' to 'sink' in cause-effect graph.

    Arguments:
      src  <str> : Source node concept (start).
      sink <str> : Sink node concept (goal).

    Returns:
      <(bool, str|[ConceptNode,])> - first item denotes whether an error occurred
      or not, the second item corresponds to an error message or a list of concept
      nodes representing the path from 'src' to 'sink' in the cause-effect graph.
    """
    if src not in self.nodes:
      return (False, 'Source %s not in Cause-Effect Graph.' % (src))
    elif sink not in self.nodes:
      return (False, 'Sink %s not in Cause-Effect Graph.' % (sink))
    else:
      return (True, bfs(self.nodes[src], self.nodes[sink]))

