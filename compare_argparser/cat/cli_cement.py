import argparse
from cement import App, Controller  # type: ignore

from .cat import cat


class CatNamespace(argparse.Namespace):
    number: bool
    FILE: list[str]


class Base(Controller):
    class Meta:  # type: ignore
        label = 'base'

        arguments = [
            (
                ['--number', '-n'],
                {'action': 'store_true'}
            ),
            (
                ['FILE'],
                {'nargs': '*', 'default': ['-']}
            )
        ]


class CatApp(App):
    class Meta:  # type: ignore
        label = 'cat'
        handlers = [Base]

    pargs: CatNamespace  # type: ignore


def main():
    with CatApp() as app:
        app.run()
        args = app.pargs

        cat(file_paths=args.FILE, has_number=args.number)


if __name__ == '__main__':
    main()
