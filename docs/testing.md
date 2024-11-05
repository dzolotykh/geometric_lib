У каждого вида объектов (`circle`, `rectangle`, `triangle`, `square`) были протестированы методы `area` и `perimeter`.

Ниже приведена неполная таблица тестов для каждого объекта, отображающая поведение на различных входных данных:

| Объект | Метод | Входные данные | Ожидаемый результат |
| --- | --- | --- | --- |
| circle | area | radius = 1 | 3.14... |
| circle | area | radius = 0 | 0 |
| circle | area | radius = -1 | ValueError |
| circle | perimeter | radius = "1" | TypeError |
| circle | perimeter | radius = 1 | 6.28... |
| circle | perimeter | radius = 0 | 0 |
| circle | perimeter | radius = -1 | ValueError |
| circle | perimeter | radius = "a" | TypeError |
| rectangle | area | width = 1, height = 1 | 1 |
| rectangle | area | width = 0, height = 1 | 0 |
| rectangle | area | width = -1, height = 1 | ValueError |
| rectangle | area | width = "a", height = 1 | TypeError |
| rectangle | area | width = 1, height = "a" | TypeError |
| rectangle | perimeter | width = 1, height = 1 | 4 |
| rectangle | perimeter | width = 0, height = 0 | 0 |
| rectangle | perimeter | width = -1, height = 1 | ValueError |
| rectangle | perimeter | width = "a", height = 1 | TypeError |
| square | area | side = 1 | 1 |
| square | area | side = 0 | 0 |
| square | area | side = -1 | ValueError |
| square | area | side = "a" | TypeError |
| square | perimeter | side = 1 | 4 |
| square | perimeter | side = 0 |
| square | perimeter | side = -1 | ValueError |
| square | perimeter | side = "a" | TypeError |
| triangle | area | side = 3, height = 4 | 6 |
| triangle | area | side = 0, height = 4 | 0 |
| triangle | area | side = -1, height = 4 | ValueError |
| triangle | area | side = "a", height = 4 | TypeError |
| triangle | perimeter | a = 3, b = 4, c = 5 | 12 |
| triangle | perimeter | a = 0, b = 4, c = 5 | 0 |
| triangle | perimeter | a = -1, b = 1, c = 1 | ValueError |
| triangle | perimeter | a = 2, b = 3, c = 228 | ValueError (треугольник не существует) |
| triangle | perimeter | a = "a", b = 4, c = 5 | TypeError |


