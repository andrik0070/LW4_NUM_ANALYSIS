from pprint import pprint
import operator

import numpy as np
from matplotlib import pyplot as plt


def euler_method(a, b, N, init, func, real_func):
    h = 0.001

    N = int((b-a)/h)

    ts = []
    ws = []
    delta = []
    number = []

    t = a
    w = init

    ts.append(t)
    ws.append(w)
    delta.append(abs(w - real_func(t, 0)))
    number.append(0)

    for i in range(1, N + 1):
        t = a + i * h
        w = w + h * func(t, w)

        ws.append(w)
        ts.append(t)
        real = real_func(t, 0)
        delta_value = abs(w - real)
        delta.append(delta_value)
        number.append(i)

        pprint('t: ' + str(t) + 'w: ' + str(w) + ' real value: ' + str(real) + ' delta:' + str(delta_value))

    return ts, ws, delta, number


if '__main__' == __name__:
    a = 1.6
    b = 0.2
    init = 1.0

    real_func = lambda t, y: (a * init * np.exp(a * t) / (a + b * init * (np.exp(a * t) - 1)))

    ts, ws, delta, number = euler_method(0, 20, 40, init, lambda t, y: a * y - b * (y ** 2), real_func)

    xs = np.linspace(0, 20, 1000)
    ys = []

    for x in xs:
        ys.append(real_func(x, 0))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, color='red')
    plt.scatter(ts, ws)
    plt.show()

    plt.xlabel('number')
    plt.ylabel('delta')
    plt.plot(number, delta, color='red')
    max_delta_index, max_delta_value = max(enumerate(delta), key=operator.itemgetter(1))
    pprint(' max_delta_value: ' + str(max_delta_value))
    plt.scatter([number[max_delta_index]], [max_delta_value], c='green')
    plt.show()
