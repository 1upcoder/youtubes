def wrapper(func):
    def function_wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return function_wrapper


@wrapper
def hello_world():
    print("hello world")


@wrapper
def pprint(message):
    print(message)

hello_world()
pprint("Junk")
pprint(message="Junk2")
