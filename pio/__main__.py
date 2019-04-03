import click

from os import getcwd

from . import lib

@click.command()
@click.argument('option', nargs=1)
@click.argument('arguments', nargs=-1)
def handler(option, arguments):
    if option == "add":
        lib.add(arguments, getcwd())
    elif option == "remove":
        lib.remove(arguments, getcwd())

if __name__ == '__main__':
    handler()