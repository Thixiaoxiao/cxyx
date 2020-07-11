import click
import sys
from importlib import import_module

sys.path.append("./")


@click.command()
@click.argument('role')
@click.argument('path')
def cxyx(role, path):
    if role == "worker" and ":" in path:
        file, obj = path.split(":")

        f = import_module(file)
        getattr(f, obj).run()


if __name__ == '__main__':
    cxyx()
