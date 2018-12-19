from pprint import pprint
import operator

import numpy as np
from matplotlib import pyplot as plt


def gear_method(a, b, N, init, func, real_func):
    h = 0.001

    N = int((b - a) / h)

    ts = []
    ws = []
    delta = []
    number = []

    t = a
    w = init

    ts.append(t)
    ws.append(w)
    number.append(0)
    delta.append(0)

    for i in range(1, 4):
        t = a + i * h
        w = w + h * func(t, w)
        ts.append(t)
        ws.append(w)
        if i != 3:
            delta.append(abs(w - real_func(t, w)))
        number.append(i)

    for i in range(4, N + 1):
        for j in range(0, 5):
            ws[i - 1] = 18 / 11 * ws[i - 2] - 9 / 11 * ws[i - 3] + 2 / 11 * ws[i - 4] + 6 / 11 * h * func(t, ws[i - 1])

        delta.append(abs(ws[i - 1] - real_func(t, w)))

        t = a + i * h
        w = w + h * func(t, ws[i - 1])

        ws.append(w)
        ts.append(t)
        number.append(i)

    delta.append(abs(ws[N - 1] - real_func(t, w)))

    return ts, ws, delta, number


if __name__ == '__main__':
    a = 1.6
    b = 0.2
    init = 1.0

    real_func = lambda t, y: (a * init * np.exp(a * t) / (a + b * init * (np.exp(a * t) - 1)))

    ts, ws, delta, number = gear_method(0, 20, 40, init, lambda t, y: a * y - b * (y ** 2), real_func)

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




