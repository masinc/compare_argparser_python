
from typing import List
from tap import Tap
from .cat import cat


class CatParser(Tap):
    number: bool = False
    FILE: List[str] = ['-']

    def configure(self) -> None:
        self.add_argument('--number', '-n')  # type: ignore
        self.add_argument('FILE', nargs='*')  # type: ignore


def main():
    parser = CatParser()
    args = parser.parse_args()

    cat(file_paths=args.FILE, has_number=args.number)


if __name__ == '__main__':
    main()
