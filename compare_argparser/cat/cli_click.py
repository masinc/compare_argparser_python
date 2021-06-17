from typing import Iterable
import click

from .cat import cat


@click.command(name='cat')
@click.option('--number', '-n', default=False, is_flag=True)
@click.argument('file', type=click.Path(), nargs=-1)
def run_cat(number: bool, file: Iterable[str]):

    file = list(file)
    if len(file) == 0:
        file = ['-']

    cat(file_paths=list(file), has_number=number)


if __name__ == '__main__':
    run_cat()
