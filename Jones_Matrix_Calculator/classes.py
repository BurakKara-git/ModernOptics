import numpy as np
from numpy import cos, sin, exp, pi


class HWP:
    def __init__(self, angle):
        radian = angle * pi / 180
        self.radian = radian
        self.M = exp(-1j * pi / 2) * np.matrix(
            [[cos(2 * radian), sin(2 * radian)], [sin(2 * radian), -cos(2 * radian)]]
        )

    def show(self):
        print(self.M)


class QWP:
    def __init__(self, angle):
        radian = angle * pi / 180
        self.radian = radian
        self.M = np.matrix(
            [
                [
                    cos(radian) ** 2 + 1j * sin(radian) ** 2,
                    (1 - 1j) * sin(radian) * cos(radian),
                ],
                [
                    (1 - 1j) * sin(radian) * cos(radian),
                    1j * cos(radian) ** 2 + sin(radian) ** 2,
                ],
            ]
        )

    def show(self):
        print(self.M)


class Mirror:
    M = np.matrix([[1, 0], [0, -1]])


class Rotator:
    def __init__(self, angle):
        radian = angle * pi / 180
        self.radian = radian
        self.M = np.matrix(
            [
                [cos(radian), sin(radian)],
                [-sin(radian), cos(radian)],
            ]
        )

    def show(self):
        print(self.M)


class LP:
    def __init__(self, angle):
        radian = angle * pi / 180
        self.radian = radian
        self.M = np.matrix(
            [
                [cos(radian) ** 2, sin(radian) * cos(radian)],
                [sin(radian) * cos(radian), sin(radian) ** 2],
            ]
        )

    def show(self):
        print(self.M)


class RCP:
    def __init__(self, angle):
        radian = angle * pi / 180
        self.radian = radian
        self.M = 0.5 * np.matrix([1, 1j], [-1j, 1])

    def show(self):
        print(self.M)


class LCP:
    def __init__(self, angle):
        radian = angle * pi / 180
        self.radian = radian
        self.M = 0.5 * np.matrix([1, -1j], [1j, 1])

    def show(self):
        print(self.M)


class EPT:
    # to be defined
    ...
