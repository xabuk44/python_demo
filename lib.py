def cashback(monthly_costs): #начало функции
    """
    >>> cashback(10_000)
    300.0
    """
    percent = 3
    result = percent * monthly_costs / 100
    return result #возврат значения, результат

def bmi(mass, height):
    """
    >>> bmi(106, 1.68) # doctest: +ELLIPSIS
    37.55...
    """
    mass_index = mass / (height * height)
    return (mass_index)

