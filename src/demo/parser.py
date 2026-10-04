import argparse

"""get a parser that can parse the command line arguments"""
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(
    '--count',
    type=int,
    default=1,
    help='the number of times to print the message'
)

parser.add_argument(
    '--message',
    type=str,
    default='Hello, World!',
    help='the message to print'
)

"""parse the command line arguments"""
args = vars(parser.parse_args())

for (k, v) in args.items():
    print(f'{k}: {v}')