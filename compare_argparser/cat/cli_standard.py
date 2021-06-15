import argparse

from .cat import cat


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='cat')
    parser.add_argument('--number', '-n', action='store_true')
    parser.add_argument('FILE', nargs='*', default=['-'])

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    cat(file_paths=args.FILE, has_show_number=args.number)


if __name__ == '__main__':
    main()
