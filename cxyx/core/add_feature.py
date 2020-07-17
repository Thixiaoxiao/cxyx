# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         add_feature
# Description:  
# Author:       Chenxiyuxiao
# Date:         2020/7/17
# -------------------------------------------------------------------------------
from cxyx.core.base import TaskBase


def do_sth_before_task(func, args, kwargs):
    if hasattr(func, "before_do_task_list"):
        for fun in func.before_do_task_list:
            fun(*args, **kwargs)


def before_do_task(func):
    def inner(fun):
        real_func = getattr(TaskBase, "task_" + func.func_name)
        if not hasattr(real_func, "before_do_task_list"):
            real_func.before_do_task_list = []
        real_func.before_do_task_list.append(fun)

    return inner


def do_sth_after_task(func, args, kwargs):
    if hasattr(func, "after_do_task_list"):
        for fun in func.after_do_task_list:
            fun(*args, **kwargs)


def after_do_task(func):
    def inner(fun):
        real_func = getattr(TaskBase, "task_" + func.func_name)
        if not hasattr(real_func, "after_do_task_list"):
            real_func.after_do_task_list = []
        real_func.after_do_task_list.append(fun)

    return inner


def do_sth_success_task(func, args, kwargs):
    if hasattr(func, "success_do_task_list"):
        for fun in func.success_do_task_list:
            fun(*args, **kwargs)


def success_do_task(func):
    def inner(fun):
        real_func = getattr(TaskBase, "task_" + func.func_name)
        if not hasattr(real_func, "success_do_task_list"):
            real_func.success_do_task_list = []
        real_func.success_do_task_list.append(fun)

    return inner


def do_sth_fail_task(func, args, kwargs):
    if hasattr(func, "fail_do_task_list"):
        for fun in func.fail_do_task_list:
            fun(*args, **kwargs)


def fail_do_task(func):
    def inner(fun):
        real_func = getattr(TaskBase, "task_" + func.func_name)
        if not hasattr(real_func, "fail_do_task_list"):
            real_func.fail_do_task_list = []
        real_func.fail_do_task_list.append(fun)

    return inner
