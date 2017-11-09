def multiply(x, y):
    try:
        ret = x * y
    except TypeError:
        ret = 0
    return ret
