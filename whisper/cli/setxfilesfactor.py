import sys
import argparse
import whisper


def create_parser():
    """ parse commandline options """

    parser = argparse.ArgumentParser(
        description='Set xFilesFactor for existing whisper file'
    )

    parser.add_argument(
        'path',
        type=str,
        help='path to whisper file'
    )

    parser.add_argument(
        'xff',
        metavar='xFilesFactor',
        type=float,
        help='new xFilesFactor, a float between 0 and 1'
    )

    return parser


def update(progname, args):
    """ Update whisper file """

    try:
        old_xff = whisper.setXFilesFactor(args.path, args.xff)
    except IOError:
        sys.stderr.write("%s: error: file '%s' does not exist\n" %
                (progname, args.path))
        sys.exit(3)
    except whisper.WhisperException as exc:
        sys.stderr.write("%s: error: %s\n" % (progname, str(exc)))
        sys.exit(4)

    print('Updated xFilesFactor: %s (%s -> %s)' %
          (args.path, old_xff, args.xff))


def main():
    parser = create_parser()
    args = parser.parse_args()
    update(parser.prog, args)


if __name__ == "__main__":
    main()
