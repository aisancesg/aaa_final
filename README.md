# aaa_final

# ИНСТРУКЦИЯ:
0) Перейти в директорию aaa_final

```
cd aaa_final
```
1) Чтобы увидеть меню, запустите команду

```
python cli.py menu
```
2) Чтобы сделать заказ, запустите команду вида:
```
python cli.py order pizza_name pizza_size [--delivery]
```
где pizza_name - наименование пиццы (доступны Margherita, Pepperoni, Hawaiian) (регистр не важен), 

pizza_size - размер пиццы (доступны L, XL),

--delivery - если хотите заказать доставку вместо самовывоза

3) Тесты запустить можно командой
```
python -m pytest testing.py
```

# Результаты
```
PS C:\Users\User\aaa_final> python cli.py menu
- Margherita 🧀: tomato sauce, mozzarella, tomatoes
- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni
- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples

PS C:\Users\User\aaa_final> python cli.py order margherita l
👨‍🍳 Приготовили за 6c!
🏠 Забрали за 59с!
PS C:\Users\User\aaa_final> python cli.py order pePPeroni xl --delivery
👨‍🍳 Приготовили за 1c!
🛵 Доставили за 76с!
PS C:\Users\User\aaa_final> python cli.py order HAWAIIAN  xl --delivery
👨‍🍳 Приготовили за 91c!
🛵 Доставили за 82с!
PS C:\Users\User\aaa_final> python cli.py order asdfghjkl l
Извините, у нас нет Asdfghjkl в меню
PS C:\Users\User\aaa_final> python cli.py order HAWAIIAN  asd --delivery
Извините, доступны только размеры L и XL
PS C:\Users\User\aaa_final> python cli.py order haWAiian xL
👨‍🍳 Приготовили за 36c!
🏠 Забрали за 1с!
```


```
PS C:\Users\User\aaa_final> python -m pytest testing.py
============================ test session starts =============================
platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0
rootdir: C:\Users\User\aaa_final
plugins: anyio-3.6.2, cov-4.1.0
collected 6 items

testing.py ......                                                       [100%] 

============================= 6 passed in 0.09s ============================== 
```
