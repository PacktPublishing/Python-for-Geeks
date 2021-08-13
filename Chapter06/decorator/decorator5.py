# decorator5.py
from datetime import datetime
from functools import wraps

def add_timestamp(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        res = "{}: {}\n".format(datetime.now(), func(*args, **kwargs))
        return res
    return inner_func

def file(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        res = func(*args, **kwargs)
        with open("log.txt", 'a') as file:
            file.write(res)
        return res
    return inner_func

def console(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res
    return inner_func

@file
@add_timestamp
def log(msg):
    return msg

@file
@console
@add_timestamp
def log1(msg):
    return msg

@console
@add_timestamp
def log2(msg):
    return msg

log("This is a test message for file only")
log1("This is a test message for both file and console")
log2("This message is for console only")