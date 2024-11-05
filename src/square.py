def area(a: float ) -> float:
    '''Принимает сторону квадрата и возвращает площадь квадрата'''
    if a < 0:
        raise ValueError("Сторона квадрата должна быть положительной")
    if type(a) not in [int, float]:
        raise TypeError("Сторона квадрата должна быть числом")
    return a * a


def perimeter(a: float) -> float:
    '''Принимает сторону квадрата и возвращает периметр квадрата'''
    if a < 0:
        raise ValueError("Сторона квадрата должна быть положительной")
    if type(a) not in [int, float]:
        raise TypeError("Сторона квадрата должна быть числом")
    return 4 * a
