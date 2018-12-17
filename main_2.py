from pprint import pprint

import numpy as np
from matplotlib import pyplot as plt

def gear_method(a, b, N, init, func, real_func):
    h = 0.01

    ts = []
    ws = []
    delta = []

    t = a
    w = init

    ts.append(t)
    ws.append(w)

    for i in range(1, 4):
        t = a + i * h
        w = w + h * func(t, w)
        ts.append(t)
        ws.append(w)

    for i in range(2, N + 1):
        for j in range(0, 5):
            ws[i+1] = 18/11*ws[i] - 9/11*ws[i - 1] + 2/11*ws[i - 2] + 6/11 * h * func(ws[i + 1])





