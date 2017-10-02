import matplotlib.pyplot as plt
import numpy as np
import math
import sys

char = 'M'
if len(sys.argv) > 1:
    char = sys.argv[1]

letter = "{0:08b}0".format(ord(char))
c = letter.count("1")


def number(i):
    return ord(i) - ord('0')


def g(t):
    return number(letter[int(t)])


def func_a(n, t):
    if t == 0:
        return 1
    return - math.cos(math.pi * n * t / 4) / (math.pi * n / 4)


def a(n):
    sum_a = 0
    for i in range(0, 8):
        a_n = func_a(n, i + 1) - func_a(n, i)
        sum_a += number(letter[i]) * a_n
    return sum_a / 4


def func_b(n, t):
    if t == 0:
        return 1
    return math.sin(math.pi * n * t / 4) / (math.pi * n / 4)


def b(n):
    sum_b = 0
    for i in range(0, 8):
        b_n = func_b(n, i + 1) - func_b(n, i)
        sum_b += number(letter[i]) * b_n
    return sum_b / 4


def f(n, t):
    if t == 0:
        return 0

    sum_x = c / 8.0
    for i in range(1, n + 1):
        sum_x += a(i) * math.sin(math.pi * i * t / 4) + b(i) * math.cos(math.pi * i * t / 4)
    return sum_x


def iterate(n, ts):
    return list(map(lambda t: f(n, t), ts))


def original(ts):
    return list(map(lambda t: g(t), ts))


def ans(ns):
    return list(map(lambda n: a(n), ns))


def bns(ns):
    return list(map(lambda n: b(n), ns))


def plot_charts(p, n, total, start = 0):
    p.subplot(total * 100 + 10 + n - start)
    p.title('{0} harmonic'.format(n))
    p.plot(ts, original(ts), 'r')
    p.plot(ts, iterate(n, ts), 'b')


ts = np.arange(0.0, 8.0, 0.01)
ns = np.arange(1, 11, 1)

print char
print ord(char)
print letter[:8]

plt.figure(1)
plt.subplots_adjust(hspace=1)
for i in range(1, 6):
    plot_charts(plt, i, 5)

plt.figure(2)
plt.subplots_adjust(hspace=1)
for i in range(6, 11):
    plot_charts(plt, i, 5, 5)

plt.figure(3)
plot_charts(plt, 128, 1, 127)

plt.figure(4)
plt.subplots_adjust(hspace=1)
plt.subplot(211)
plt.title('a values')
plt.xlabel('harmonic number')
plt.ylabel('amplitude')
plt.bar(ns, ans(ns), 0.2)
plt.grid(True, which='both')

plt.subplot(212)
plt.title('b values')
plt.xlabel('harmonic number')
plt.ylabel('amplitude')
plt.bar(ns, bns(ns), 0.2)
plt.grid(True, which='both')

plt.show()