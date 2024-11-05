import math


def area(r: float) -> float:
    '''Принимает радиус окружности и возвращает площадь окружности'''
    if r < 0:
        raise ValueError('Радиус должен быть неотрицательным')
    if type(r) not in [int, float]:
        raise TypeError('Радиус должен быть числом')
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус окружности и возвращает длину окружности'''
    if r < 0:
        raise ValueError('Радиус должен быть неотрицательным')
    if type(r) not in [int, float]:
        raise TypeError('Радиус должен быть числом')
    return 2 * math.pi * r

