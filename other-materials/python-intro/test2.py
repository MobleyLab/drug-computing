def multiply(x, y):
    try:
        ret = x * y
    except StandardError:
        ret = 0
    return ret
