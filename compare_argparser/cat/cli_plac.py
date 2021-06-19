from typing import List
import plac  # type: ignore
from .cat import cat


@plac.flg('number')  # type: ignore
@plac.pos('FILE')  # type: ignore
def run(number: bool, *FILE: str):
    files: List[str] = ['-'] if len(FILE) == 0 else list(FILE)

    cat(file_paths=files, has_number=number)


if __name__ == '__main__':
    plac.call(run)  # type: ignore
