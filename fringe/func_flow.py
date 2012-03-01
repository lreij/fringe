# -*- coding:utf-8 -*-
## Jerry Lu <lreij@163.com>
import functools

CALL_LEVEL = 0


def func_flow(f):

    @functools.wraps(f)
    def wrapper(*args, **kw):
        log = ""
        if hasattr(f, '__module__'):
            log += str(f.__module__)
            log += ' '
        if len(args) > 0:
            if hasattr(args[0], '__class__'):
                if 'type' not in str(args[0].__class__):
                    log += str(args[0].__class__)
                    log += '.'
            else:
                log += ' function '
        if hasattr(f, '__name__'):
            log += str(f.__name__)
        global CALL_LEVEL
        print '--' * CALL_LEVEL, log, ' start'
        CALL_LEVEL += 1
        r = f(*args, **kw)
        CALL_LEVEL -= 1
        print '--' * CALL_LEVEL, log, ' end'
        print
        return r

    return wrapper
