# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""


def is_permutation(a: str, b: str) -> bool:
    if a == b:
        return True
    return False


assert is_permutation("baba", "abab")  # True
assert is_permutation("abbba", "abab")  # False
