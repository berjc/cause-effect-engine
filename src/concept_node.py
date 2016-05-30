"""
'concept_node.py' implements the ConceptNode class.
"""

class ConceptNode:
  """
  Implements a concept node in the Cause-Effect graph.

  Attributes:
    concept <str>    : Describes meaning of concept node.
    causes  <[str,]> : List of causes of concept node.
    effects <[str,]> : List of effects caused by concept node.
  """

  def __init__(self, concept):
    """
    Initializes ConceptNode.

    Argument:
      concept <str> : Describes meaning of concept node.
    """
    self.concept = concept
    self.causes = []
    self.effects = []

  def __str__(self):
    """
    Returns string representation of concept node.

    Returns:
      <str> - string representation of concept node.
    """
    return 'Concept \'%s\'' % (self.concept)

  def add_cause(self, cause_node):
    """
    Adds cause to concept node's causes.

    Argument:
      cause_node <ConceptNode> : Concept node to add as cause to this concept node.
    """
    self.causes.append(cause_node)

  def add_effect(self, effect_node):
    """
    Adds effect to concept node's effects.

    Argument:
      effect_node <ConceptNode> : Concept node to add as effect to this concept node.
    """
    self.effects.append(effect_node)

