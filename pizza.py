class Pizza:
    """
    Класс с базовой информацией о пицце
    """
    def __init__(self, name: str = '', icon: str = '', size: str = 'L') \
            -> None:
        """ Инициализирует пиццу """
        self.name = name.capitalize()
        self.size = size.upper()
        self.icon = icon
        self.recipe: list = []

    def dict(self) -> dict:
        """
        Выводит рецепт пиццы в виде словаря,
        где ключ = название пиццы, значение = рецепт
        """
        return {self.name: self.recipe}

    def __eq__(self, other) -> bool:  # бонус
        """ Выясняет, одинаковы ли пиццы """
        if not isinstance(other, Pizza):
            print(f'{other} не является пиццей')
            return False
        return ((self.name == other.name)
                and (self.size == other.size)
                and set(self.recipe) == set(other.recipe))


class Margherita(Pizza):
    """pizza Margherita"""
    def __init__(self, size: str = 'L'):
        super().__init__('Margherita', '🧀', size)
        self.recipe = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):
    """pizza Pepperoni"""
    def __init__(self, size: str = 'L'):
        super().__init__('Pepperoni', '🍕', size)
        self.recipe = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):
    """pizza Hawaiian"""
    def __init__(self, size: str = 'L'):
        super().__init__('Hawaiian', '🍍', size)
        self.recipe = ['tomato sauce', 'mozzarella',
                       'chicken', 'pineapples']
