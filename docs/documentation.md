# Библиотека для работы с геометрическими фигурами

## Модуль circle.py
### Функция area(r: float) -> float
Вычисляет площадь круга с радиусом r. 
Пример использования:
```python
from circle import area
area(5) # 78.53...
```

### Функция perimeter(r: float) -> float
Вычисляет периметр круга с радиусом r.
Пример использования:
```python
from circle import perimeter
perimeter(5) # 31.41...
```

## Модуль rectangle.py
### Функция area(a: float, b: float) -> float
Вычисляет площадь прямоугольника со сторонами a и b.
Пример использования:
```python
from rectangle import area
area(5, 10) # 50
```

### Функция perimeter(a: float, b: float) -> float
Вычисляет периметр прямоугольника со сторонами a и b.
Пример использования:
```python
from rectangle import perimeter
perimeter(5, 10) # 30
```

## Модуль square.py
### Функция area(a: float) -> float
Вычисляет площадь квадрата со стороной a.
Пример использования:
```python
from square import area
area(5) # 25
```

### Функция perimeter(a: float) -> float
Вычисляет периметр квадрата со стороной a.
Пример использования:
```python
from square import perimeter
perimeter(5) # 20
```
## Модуль triangle.py
### Функция area(a: float, b: float, c: float) -> float
Вычисляет площадь треугольника со сторонами a, b и c.
Пример использования:
```python
from triangle import area
area(3, 4, 5) # 6.0
```

### Функция perimeter(a: float, b: float, c: float) -> float
Вычисляет периметр треугольника со сторонами a, b и c.
Пример использования:
```python
from triangle import perimeter
perimeter(3, 4, 5) # 12
```

## Список коммитов:
```shell
a4ba3b0 (HEAD -> new_features_439609, origin/new_features_439609) add triangle & fix rectangle
d402c07 add rectangle.py
d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
8ba9aeb L-03: Circle and square added
```
