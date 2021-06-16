import sys
from typing import List, Iterator, Optional, TextIO


def cat(file_paths: Optional[List[str]] = [],
        has_number: Optional[bool] = None):

    def file_lines(file: TextIO) -> Iterator[str]:
        for line in file:
            yield line

    def print_file(file: TextIO, initial_line_number: int = 1) -> Optional[int]:
        line_number: Optional[int] = None
        for (index, line) in enumerate(file_lines(file)):
            out: str

            if has_number:
                line_number = initial_line_number + index
                out = f'{line_number}\t{line}'
            else:
                out = line
            print(out, end='')

        return line_number

    def cat_core(file_path: str, initial_line_number: int = 1) -> Optional[int]:
        file: TextIO
        if file_path == '-':
            if sys.stdin.isatty():
                return initial_line_number
            file = sys.stdin
        else:
            file = open(file_path)

        with file:
            return print_file(file, initial_line_number)

    if not file_paths:
        file_paths = []
    if len(file_paths) == 0:
        file_paths = ['-']

    line_number: int = 0
    for file_path in file_paths:
        if has_number:
            line_number += 1

        line_number = cat_core(file_path, initial_line_number=line_number) or 1
