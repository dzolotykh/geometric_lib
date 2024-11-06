У каждого вида объектов ([`circle`](../src/circle.py), [`rectangle`](../src/rectangle.py), [`triangle`](../src/triangle.py), [`square`](../src/square.py)) были протестированы методы `area` и `perimeter`.

Ниже приведена неполная таблица тестов для каждого объекта, отображающая поведение на различных входных данных:

| Объект | Метод | Входные данные | Ожидаемый результат | Была ошибка? |
| --- | --- | --- | --- | --- |
| circle | area | radius = 1 | 3.14... | Нет |
| circle | area | radius = 0 | 0 | Да |
| circle | area | radius = -1 | ValueError | Да |
| circle | perimeter | radius = "1" | TypeError | Да |
| circle | perimeter | radius = 1 | 6.28... | Нет |
| circle | perimeter | radius = 0 | 0 | Да |
| circle | perimeter | radius = -1 | ValueError | Да |
| circle | perimeter | radius = "a" | TypeError | Да |
| rectangle | area | width = 1, height = 1 | 1 | Нет |
| rectangle | area | width = 0, height = 1 | 0 | Да |
| rectangle | area | width = -1, height = 1 | ValueError | Да |
| rectangle | area | width = "a", height = 1 | TypeError | Да |
| rectangle | area | width = 1, height = "a" | TypeError | Да |
| rectangle | perimeter | width = 1, height = 1 | 4 | Нет |
| rectangle | perimeter | width = 0, height = 0 | 0 | Да |
| rectangle | perimeter | width = -1, height = 1 | ValueError | Да |
| rectangle | perimeter | width = "a", height = 1 | TypeError | Да |
| square | area | side = 1 | 1 | Нет |
| square | area | side = 0 | 0 | Да |
| square | area | side = -1 | ValueError | Да |
| square | area | side = "a" | TypeError | Да |
| square | perimeter | side = 1 | 4 | Нет |
| square | perimeter | side = 0 | 0 | Да |
| square | perimeter | side = -1 | ValueError | Да |
| square | perimeter | side = "a" | TypeError | Да |
| triangle | area | side = 3, height = 4 | 6 | Нет |
| triangle | area | side = 0, height = 4 | 0 | Да |
| triangle | area | side = -1, height = 4 | ValueError | Да |
| triangle | area | side = "a", height = 4 | TypeError | Да |
| triangle | perimeter | a = 3, b = 4, c = 5 | 12 | Нет |
| triangle | perimeter | a = 0, b = 4, c = 5 | 0 | Да |
| triangle | perimeter | a = -1, b = 1, c = 1 | ValueError | Да |
| triangle | perimeter | a = 2, b = 3, c = 228 | ValueError (треугольник не существует) | Да |
| triangle | perimeter | a = "a", b = 4, c = 5 | TypeError | Да |


