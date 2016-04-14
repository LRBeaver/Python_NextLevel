__author__ = 'lyndsay.beaver'

import math
import time

def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    print "Hit DB"
    return z

def test_russian():
    start_time = time.time()
    print(russian(357, 16))
    print("Russian Algorithm took %f seconds" % (time.time()-start_time))
    assert russian(357, 16) == 5712

if __name__ == "__main__":
    test_russian()


