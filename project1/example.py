import time


def step1():
    print("I am running for a while in step 1")

    iters = 0
    while iters < 10:
        print("iter: ", iters)
        iters += 1
        time.sleep(10)


def step2():
    print("I am running for a while in step 2")

    iters = 0
    while iters < 10:
        print("iter: ", iters)
        iters += 1
        time.sleep(10)
