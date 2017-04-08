import os
import sys
import signal
import optparse

try:
  import whisper
except ImportError:
  raise SystemExit('[ERROR] Please make sure whisper is installed properly')

# Ignore SIGPIPE
try:
  signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except AttributeError:
  #windows?
  pass


def create_parser():
    option_parser = optparse.OptionParser(
        usage='%%prog path <%s> [xFilesFactor]' % '|'.join(whisper.aggregationMethods))

    return option_parser


def update(args):
    path = args[0]
    aggregationMethod = args[1]

    xFilesFactor = None
    if len(args) == 3:
      xFilesFactor = args[2]

    try:
      oldAggregationMethod = whisper.setAggregationMethod(path, aggregationMethod, xFilesFactor)
    except IOError:
      sys.stderr.write("[ERROR] File '%s' does not exist!\n" % path)
      sys.exit(1)
    except whisper.WhisperException as exc:
      sys.stderr.write('error: %s\n' % str(exc))
      #sys.stderr.write("[ERROR] File '%s' does not exist!\n\n" % path)
      sys.exit(4)

    print('Updated aggregation method: %s (%s -> %s)' % (path,oldAggregationMethod,aggregationMethod))


def main():
    parser = create_parser()
    (options, args) = parser.parse_args()

    if len(args) < 2:
      parser.print_help()
      sys.exit(1)

    update(args)


if __name__ == "__main__":
    main()
