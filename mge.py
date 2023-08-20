# Matrix Game Engine module
# смотри в вики Камень Ножницы Бумага
# see wiki Rock Paper Scissors

from collections.abc import Iterable


class MetrixGameEngine:
    """Движок для матричных игр типа камень->ножницы->бумага.
    Engine for matrix games like rock->scissors->paper."""
    def __init__(self, figure_names: Iterable):
        # фигуры. нечетное число не менее трех и не более пяти!
        # ключом словаря является имя фигуры
        # figures. an odd number not less than three and not more than five!
        # the key of the dictionary is the figure name
        self._figures = {key: None for key in figure_names}
        if len(self._figures) not in (3, 5):
            raise ValueError(f"Invalid count figures: {len(self._figures)}")

    def make_losers(self, key, keys_of_the_losers: Iterable):
        """Добавляет в словарь _figures список ключей фигур, которые проигрывают фигуре с ключем key, как значение
        Adds to the _figures dictionary a list of figure keys that play the figure with key key as value"""
        self._figures[key] = [_key for _key in keys_of_the_losers]

    def _is_it_a_loser(self, key, key_for_check) -> bool:
        """Является ли фигура с ключом key_for_check по отношению к фигуре key, проигравшей?
        Is the figure with key key_for_check against the key figure losing?"""
        return key_for_check in self._figures[key]

    def figures(self):
        """Функция-генератор. Возвращает ключи фигур.
        Generator function. Returns figure keys"""
        for key in self._figures:
            yield key

    def solve(self, figure_key_0, figure_key_1) -> [object, None]:
        """Решает, какой ключ из key_0 и key_1 выиграл. В случае ничьи возвращает None,
        иначе возвращает ключ фигуры-победителя.
        Decides which key from key_0 and key_1 won. Returns None in case of a tie,
        otherwise returns the key of the winning figure."""
        if figure_key_0 == figure_key_1:
            return None
        if self._is_it_a_loser(figure_key_0, figure_key_1):
            return figure_key_0
        if self._is_it_a_loser(figure_key_1, figure_key_0):
            return figure_key_1
