def divide(first, second):  # зададим ф-ию прин-ую 2 парам.
    if second == 0:         # если парам. равен 0
        return 'Ошибка'     # то, вернется 'Ошибка' - т.к. на 0  делить нельзя
    return first / second   # если second не равен 0, то выполнится деление