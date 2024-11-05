def area(a: float, b: float) -> float: 
    '''
    Возвращает площадь прямоугольника
    
        Параметры:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника

        Возвращаемое значение:
            int: площадь прямоугольника со сторонами a и b
    '''

    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника должны быть положительными")
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Стороны прямоугольника должны быть числами")
    return a * b 

def perimeter(a: float, b: float) -> float: 
    '''Принимает длины сторон прямоугольника и возвращает периметр прямоугольника'''

    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника должны быть положительными")
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Стороны прямоугольника должны быть числами")
    if a == 0 or b == 0:
        return 0
    return 2* (a + b) 
