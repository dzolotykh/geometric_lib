def area(a: float, h: float) -> float: 
    '''
    Принимает сторону и высоту треугольника и возвращает площадь треугольника
    
        Параметры:
                a (float): сторона треугольника
                h (float): высота треугольника
        
        Возвращаемое значение:
                float: площадь треугольника со стороной a и высотой h
    '''

    if a < 0 or h < 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if type(a) not in [int, float] or type(h) not in [int, float]:
        raise TypeError("Стороны треугольника должны быть числами")
    return a * h / 2 

def perimeter(a: float, b: float, c: float) -> float: 
    '''
    Принимает стороны треугольника и возвращает периметр треугольника

        Параметры:
                a (float): сторона треугольника
                b (float): сторона треугольника
                c (float): сторона треугольника

        Возвращаемое значение:
                float: периметр треугольника со сторонами a, b и c
    '''

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
        raise TypeError("Стороны треугольника должны быть числами")
    if a == 0 or b == 0 or c == 0:
        return 0
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    return a + b + c
