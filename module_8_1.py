from typing import Union
def add_everything_up(a, b) -> Union[int, float, str]:
    try:
        return f'{a + b:0.3f}'
    except TypeError:
        return f'{a}{b}'



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


