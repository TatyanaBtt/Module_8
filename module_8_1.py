def add_everything_up(a:(int or float or str), b:(int or float or str)):
    try:
        a + b
    except TypeError:
        return f'{a}{b}'
    else:
        return f'{a+b:0.3f}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


