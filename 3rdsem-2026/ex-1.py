#decorators
# to enchance the functionality of existing functions, we use decorators
import time
# app - 1.12.12
# whatsup app - 12
# 



def profiling(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Total time taken in {}: {}'
              .format(func.__name__, end_time - start_time))
        return result
    return wrapper



@profiling
def display_info():
    for i in range(3):
        time.sleep(1)
        print('running display_info')

# c = profiling(display_info)
# c()

# calculator(1, 2, 3, operator="+", display=True)
@profiling
def add(*args):
    time.sleep(2)
    return sum(args)


d = profiling(add)
d(1, 2, 3, 4, 5)

#def calculator(*args, operator="+")
# def calculator(operator="+")
#def calculator(**operator)
display_info()
add(1, 2, 3, 4, 5)
