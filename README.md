<h2>Test-project</h2>


<b>Project1</b> - библиотека по вычислению площади геометрических фигур<br>

<div>:large_blue_diamond:Основной функционал:large_blue_diamond:<br>
<ul>
    <li>Вычисление площади круга по радиусу</li>
    <li>Вычисление площади треугольника по трём сторонам</li>
    <li>Вычисление площади фигуры без знания типа фигуры в compile-time</li>
</ul>
</div><br>
<div>:small_blue_diamond:Добавленные особенности:small_blue_diamond:<br>
<ul>
    <li>Покрытие кода юнит-тестами</li>
    <li>Проверка на то, является ли треугольник прямоугольным</li>
</ul>
</div><br>
<hr>
<div>
<b>Project2</b> - PySpark приложение<br>

<div>:large_blue_diamond:Функционал:large_blue_diamond:<br>
Возвращение датафрейма, который вернёт все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.

</div>
<br>
<h3>Локальное развёртывание проекта на ОС Windows</h3>

```cmd
    git clone https://github.com/735Andrew/Test-project
    cd Test-project 
    python -m venv venv 
    venv\Scripts\activate
    (venv) pip install -r requirements.txt
    
    (venv) python project1\menu.py # Запуск меню для вычисления площадей фигур
	
    (venv) spark-submit project2\pyspark_dataframe.py # Необходима предустановленная Java 
    
```
</div>
<hr>