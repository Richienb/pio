import click

from os import getcwd

from . import lib


@click.command()
@click.argument('option', nargs=1)
@click.argument('arguments', nargs=-1)
def handler(option, arguments):
    d = {
        'add': lib.add,
        'remove': lib.remove,
        'install': lib.install,
        'update': lib.update
    }
    d.get(option)(arguments, getcwd())


if __name__ == '__main__':
    handler()
