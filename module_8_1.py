def add_everything_up(a, b):
    try:
        result = round(a + b, 3)
        return result
    except TypeError:
        print(a, end = '')
        print(b, end = '')
        return ''
 
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
