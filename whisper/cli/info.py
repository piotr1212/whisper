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
  #OS=windows
  pass

def create_parser():
    option_parser = optparse.OptionParser(usage='''%prog path [field]''')

    return option_parser

def info(args):
    path = args[0]
    if len(args) > 1:
      field = args[1]
    else:
      field = None

    try:
      info = whisper.info(path)
    except whisper.WhisperException as exc:
      raise SystemExit('[ERROR] %s' % str(exc))

    info['fileSize'] = os.stat(path).st_size

    if field:
      if field not in info:
        print('Unknown field "%s". Valid fields are %s' % (field, ','.join(info)))
        sys.exit(1)

      print(info[field])
      sys.exit(0)


    archives = info.pop('archives')
    for key,value in info.items():
      print('%s: %s' % (key,value))
    print

    for i,archive in enumerate(archives):
      print('Archive %d' % i)
      for key,value in archive.items():
        print('%s: %s' % (key,value))
      print


def main():
    parser = create_parser()
    (options, args) = parser.parse_args()

    if len(args) < 1:
      parser.print_help()
      sys.exit(1)


if __name__ == "__main__":
    main()
