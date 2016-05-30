"""
'utils.py' implements utility methods for the Cause-Effect-Engine.
"""

# Terminal Colors
HEADERC = '\033[95m'
OKBLUEC = '\033[94m'
OKGREENC = '\033[92m'
WARNINGC = '\033[93m'
FAILC = '\033[91m'
ENDC = '\033[0m'

def print_error(error_msg):
  """
  Prints error message.

  Argument:
    error_msg <str> : Error message to display.
  """
  print '%sERROR:%s %s%s%s' % (FAILC, ENDC, error_msg, WARNINGC, ENDC)

def print_path(path):
  """
  Prints cause-effect path.

  Argument:
    path <[ConceptNode,]> : List of concept nodes to print.
  """
  print 'Source Cause %s\'%s\'%s' % (OKGREENC, path[0].concept, ENDC)
  for concept in path[1:-1]:
    print '  %sleads to%s %s' % (OKBLUEC, ENDC, concept)
  print 'Sink Effect %s\'%s\'%s' % (OKGREENC, path[-1].concept, ENDC)

