"""
'engine.py' implements the driver for the Cause-Effect-Engine.
"""

from sys      import exit
from ceg      import CEGraph
from optparse import OptionParser
from utils    import print_error, print_path

def main():
  # Setup option parser
  parser = OptionParser()
  parser.add_option('-f', '--file', dest='fname',
    help='read cause-effect pairs from FILE', metavar='FILE')

  # Interpret options passed
  (opts, args) = parser.parse_args()
  if not opts.fname:
    parser.error('File not provided. Use --file option.')

  ceg = CEGraph()  # Initialize cause-effect graph

  # Read file of cause-effect pairs
  with open(opts.fname, 'r') as f:
    for line in f:
      cause, effect = line.rstrip().split()
      res = ceg.add(cause, effect)
      if not res[0]:
        print_error(res[1])

  while True:
    try:
      src = raw_input('Source: ')
      sink = raw_input('Sink:   ')
      res = ceg.resolve(src, sink)
      if res[0] and res[1]:
        print_path(res[1])
      elif not res[1]:
        print_error('No path found.')
      else:
        print_error(res[1])
    except KeyboardInterrupt:
      print
      exit('Goodbye!')

if __name__ == '__main__':
  main()

