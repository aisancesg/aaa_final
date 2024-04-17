import click
from pizza import Pizza, Margherita, Pepperoni, Hawaiian
from decorator import log
from typing import Any


@log('👨‍🍳 Приготовили за {}c!')
def bake(pizza: Pizza) -> None:  # не надо было сейчас реализовывать
    """Готовит пиццу"""
    pass


@log('🛵 Доставили за {}с!')
def delivery_(pizza: Pizza) -> None:  # не надо было сейчас реализовывать
    """Доставляет пиццу"""
    pass


@log('🏠 Забрали за {}с!')
def pickup(pizza: Pizza) -> None:  # не надо было сейчас реализовывать
    """Самовывоз"""
    pass


@click.group()
def cli() -> None:
    """
    Посмотрите на меню и выберете пиццу.
    Доступны доставка и самовывоз.
    """
    pass


@cli.command()
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
@click.option('--delivery', default=False, is_flag=True)
def order(pizza: str, size: str, delivery: bool) -> None:
    """Готовит и доставляет(если нужно) пиццу"""
    pizza = pizza.capitalize()
    if pizza not in ['Margherita', 'Pepperoni', 'Hawaiian']:
        print(f'Извините, у нас нет {pizza} в меню')
        return
    if size.upper() not in ['L', 'XL']:
        print('Извините, доступны только размеры L и XL')
        return

    your_pizza: Any = None
    if pizza == 'Margherita':
        your_pizza = Margherita()
    elif pizza == 'Pepperoni':
        your_pizza = Pepperoni()
    else:
        your_pizza = Hawaiian()
    bake(your_pizza)

    if delivery:
        delivery_(your_pizza)
    else:
        pickup(your_pizza)


@cli.command()
def menu():
    """Выводит меню"""
    pizzas = [Margherita(), Pepperoni(), Hawaiian()]
    for pizza in pizzas:
        recipe_str = ', '.join(pizza.recipe)
        print(f'- {pizza.name} {pizza.icon}: {recipe_str}')


if __name__ == '__main__':
    cli()
