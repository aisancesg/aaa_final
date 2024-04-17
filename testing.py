from cli import cli
from click.testing import CliRunner


def test_menu():
    """
    Тестируем, верное ли меню выдается.
    # смотрела про CliRunner на
    # https://stackoverflow.com/questions/45235045/how-do-i-use-clirunner-to-test-a-script
    """
    result = CliRunner().invoke(cli, ['menu'])
    assert (result.output ==
            ('- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n'
             '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n'
             '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'))


def test_correct_order_1():
    """Правильно ли обрабатывается корректный заказ"""
    arguments = ['order', 'margherita', 'L', '--delivery']
    result = CliRunner().invoke(cli, arguments)
    assert '👨‍🍳 Приготовили за' in result.output
    assert '🛵 Доставили за' in result.output


def test_correct_order_2():
    """Правильно ли обрабатывается корректный заказ"""
    arguments = ['order', 'PEPPERONI', 'XL']
    result = CliRunner().invoke(cli, arguments)
    assert '👨‍🍳 Приготовили за' in result.output
    assert '🏠 Забрали за' in result.output


def test_correct_order_3():
    """Правильно ли обрабатывается корректный заказ"""
    arguments = ['order', 'haWAiian', 'l']
    result = CliRunner().invoke(cli, arguments)
    assert '👨‍🍳 Приготовили за' in result.output
    assert '🏠 Забрали за' in result.output


def test_incorrect_name_order():
    """
    Проверяем, правильно ли обрабатывается заказ
    с отсутствующим у нас наименованием пиццы
    """
    arguments = ['order', 'sdfghjk', 'l']
    result = CliRunner().invoke(cli, arguments)
    assert (f'Извините, у нас нет {arguments[1].capitalize()} в меню\n' ==
            result.output)


def test_incorrect_size_order():
    """
    Проверяем, правильно ли обрабатывается заказ
    с отсутствующим у нас размером пиццы
    """
    arguments = ['order', 'hawaiian', 'm']
    result = CliRunner().invoke(cli, arguments)
    assert 'Извините, доступны только размеры L и XL\n' == result.output
