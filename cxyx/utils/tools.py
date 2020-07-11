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
        worker = getattr(f, obj)
        worker.logger.info("Worker start to work -------------------------")
        worker.run()


if __name__ == '__main__':
    cxyx()
