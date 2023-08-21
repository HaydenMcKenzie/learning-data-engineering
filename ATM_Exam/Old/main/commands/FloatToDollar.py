def dollarAdd(x, y):
    """
    :param x: First input
    :param y: Second input
    :return: Adds both numbers and returns a number with $ and a max of 2 decimals - e.g. 1 + 1 = $2.00
    """
    return f'{x + y:.2f}'

#"$" + f'{x + y:.2f}'

def dollarMinus(x, y):
    """
    :param x: First input
    :param y: Second input
    :return: Minuses both numbers and returns a number with $ and a max of 2 decimals - e.g. 2 - 1 = $1.00
    """
    return f'{x - y:.2f}'

