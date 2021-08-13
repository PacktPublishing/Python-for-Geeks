# decorator1.py

def add_hello(myfunc):
    def _add_hello():
        print("inside add hello")
        myfunc()
    return _add_hello

@add_hello
def hello_world():
    print("hello world")

hello_world()