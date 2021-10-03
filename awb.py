from __future__ import (
    division, absolute_import, print_function, unicode_literals)

import cv2 as cv
import numpy as np
import timeit

def show(final):
    print('display')
    cv.imshow('Temple', final)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Insert any filename with path
img = cv.imread('0.jpg')

def white_balance(img):
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB) #CIELAB  model
    avg_a = np.average(result[:, :, 1]) #a
    avg_b = np.average(result[:, :, 2]) #b
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
    return result

final = np.hstack((img, white_balance(img)))
show(final)
cv.imwrite('result.jpg', final)

setup = '''
from  __main__ import white_balance
import cv2 as cv
img = cv.imread('0.jpg')
'''
number = 100
t = timeit.timeit(stmt="white_balance(img)", setup=setup, number=number)
print(t/number)