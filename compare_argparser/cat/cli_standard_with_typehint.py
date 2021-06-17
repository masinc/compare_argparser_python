import argparse

from .cat import cat
from .cli_standard import create_parser


class PaserResult(argparse.Namespace):
    number: bool
    FILE: list[str]


def main():
    parser = create_parser()
    args: PaserResult = parser.parse_args(namespace=PaserResult())
    cat(file_paths=args.FILE, has_number=args.number)


if __name__ == '__main__':
    main()
