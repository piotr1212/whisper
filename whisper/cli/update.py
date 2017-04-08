import sys
import time
import signal
import optparse

try:
  import whisper
except ImportError:
  raise SystemExit('[ERROR] Please make sure whisper is installed properly')

# Ignore SIGPIPE
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

now = int( time.time() )


def create_parser():
    option_parser = optparse.OptionParser(
        usage='''%prog [options] path timestamp:value [timestamp:value]*''')

    return option_parser


def update(options, args):
    if len(args) < 2:
      return 1

    path = args[0]
    datapoint_strings = args[1:]
    datapoint_strings = [point.replace('N:', '%d:' % now)
                         for point in datapoint_strings]
    datapoints = [tuple(point.split(':')) for point in datapoint_strings]

    try:
      if len(datapoints) == 1:
        timestamp,value = datapoints[0]
        whisper.update(path, value, timestamp)
      else:
        whisper.update_many(path, datapoints)
    except whisper.WhisperException as exc:
      raise SystemExit('[ERROR] %s' % str(exc))


def main():
    parser = create_parser()
    (options, args) = parser.parse_args()
    if update(options, args):
        parser.print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
