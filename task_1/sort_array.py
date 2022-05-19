from random import randint


def sort(data):
    """Function that sorts an array using
    QuickSort algorithm"""
    if len(data) < 2:
        return data

    lower_numbers = []
    same_numbers = []
    higher_numbers = []

    pivot = data[randint(0, len(data) - 1)]

    for number in data:
        if number < pivot:
            lower_numbers.append(number)
        elif number == pivot:
            same_numbers.append(number)
        elif number > pivot:
            higher_numbers.append(number)

    return sort(lower_numbers) + same_numbers + sort(higher_numbers)


if '__main__' == __name__:
    print(sort([2, 3, 532, 2, 5, 235, 4, 3, 6, 43, 634, 3, 643, ]))
