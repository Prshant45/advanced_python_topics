# decorator - function that takes another function as an argument
#  and extends the behavior of the latter function
#  without explicitly modifying it.
import time

def profiling_decorator(parameter):
    print(parameter)
    def inner1(func):
        def inner(*args, **kwargs):
            before = time.time()
            func(*args, **kwargs)
            diff = time.time() - before
            print(f"time taken: {diff}")
        return inner
    return inner1

@profiling_decorator("demo")
def print_function():
    for i in range(5):
        time.sleep(1)
        print("Hello, World!")

# new_func = profiling_decorator(print_function)
# new_func()



print_function()