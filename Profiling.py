import time

def function1():
    time.sleep(1)
    print("function1 completed!")

def function2():
    time.sleep(3)
    print("function2 completed!")

def function3():
    time.sleep(7)
    print("function3 completed!")

function1()
function2()
function3()  

# Profile the code using python -m cProfile -s cumtime Profiling.py'