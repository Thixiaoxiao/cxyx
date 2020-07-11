import click
import sys
from importlib import import_module

# from multiprocessing import Process

sys.path.append("./")


@click.command()
@click.argument('role')
@click.argument('path')
@click.option('--worker_number', prompt='worker_num', default=1,
              help='The number of workers in one process.')
# @click.option('--process_number', prompt='process_num', default=1,
#               help='The number of process.')
def cxyx(role, path, worker_number,
         # process_number
         ):
    if role == "worker" and ":" in path:
        def parse_in_one_process(path, worker_number):
            file, obj = path.split(":")

            f = import_module(file)
            worker = getattr(f, obj)
            if worker_number == 1:
                worker.run()
            else:
                worker.run_with_many_process(worker_number)

        parse_in_one_process(path, worker_number)
        # if process_number == 1:
        #     parse_in_one_process(path, worker_number)
        # else:
        #     tasks = [
        #         Process(target=parse_in_one_process, args=(path, worker_number))
        #         for _ in range(process_number)
        #     ]
        #     for task in tasks:
        #         task.start()
        #     for task in tasks:
        #         task.join()


if __name__ == '__main__':
    cxyx()
