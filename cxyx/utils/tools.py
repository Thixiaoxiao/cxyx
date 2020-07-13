import click
import sys
from importlib import import_module

# from multiprocessing import Process

sys.path.append("./")
print(r"""
                            _ooOoo_
                           o8888888o
                           88" . "88
                           (| -_- |)
                            O\ = /O
                        ____/`---'\____
                      .   ' \\| |// `.
                       / \\||| : |||// \
                     / _||||| -:- |||||- \
                       | | \\\ - /// | |
                     | \_| ''\---/'' | |
                      \ .-\__ `-` ___/-. /
                   ___`. .' /--.--\ `. . __
                ."" '< `.___\_<|>_/___.' >'"".
               | | : `- \`.;`\ _ /`;.`/ - ` : | |
                 \ \ `-. \_ __\ /__ _/ .-` / /
         ======`-.____`-.___\_____/___.-`____.-'======
                            `=---='
         .............................................
                  佛祖镇楼                  BUG辟易
          佛曰:
                  写字楼里写字间，写字间里程序员；
                  程序人员写程序，又拿程序换酒钱。
                  酒醒只在网上坐，酒醉还来网下眠；
                  酒醉酒醒日复日，网上网下年复年。
                  但愿老死电脑间，不愿鞠躬老板前；
                  奔驰宝马贵者趣，公交自行程序员。
                  别人笑我忒疯癫，我笑自己命太贱；
                  不见满街漂亮妹，哪个归得程序员？
Welcome to use CXYX !         
        """)


@click.command()
@click.argument('role')
@click.argument('path')
@click.option('--worker_number', default=1,
              help='The number of workers in one process.')
# @click.option('--process_number', default=1,
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
