from functools import wraps
from random import randint


def log(pattern: str):  # бонусный вариант декоратора
    """
    Декоратор принимает шаблон в виде 'текст {}c!',
    в который подставляется время внутрь фигурных скобок{}.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time = randint(1, 100)  # сказали, что достаточно имитации времени
            print(pattern.format(time))
        return wrapper
    return decorator
