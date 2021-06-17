import fire  # type: ignore
from .cat import cat


def run_cat(number: bool = False, *FILE: str):
    print(f"{number=}")
    print(f"{FILE=}")

    cat(file_paths=list(FILE), has_number=number)


def main():
    fire.Fire(run_cat)  # type: ignore


if __name__ == '__main__':
    main()
