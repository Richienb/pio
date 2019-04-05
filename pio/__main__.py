import click

from os import getcwd

import pio as lib


@click.command()
@click.argument("option", nargs=1)
@click.argument("arguments", nargs=-1)
def handler(option, arguments):
    getattr(lib, option)(getcwd(), arguments)


if __name__ == "__main__":
    handler()
