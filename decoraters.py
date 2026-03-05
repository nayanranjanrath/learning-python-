import time


def timer(func):
    start =time.time()
    def wraper(*args):
        result =func(*args)
        end =time.time()
        print(f"time required to execute the functinom{func.__name__}is{end-start}seconds")
        return result
    return wraper
@timer
def example():
    time.sleep(5)

example()