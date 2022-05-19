def is_palindrome(value: str) -> bool:
    """Function that returns is given
    number is palindrome"""
    if value == value[::-1]:
        return True
    return False


def get_length(string: str) -> int:
    """Function that recursively counts
    length of the string"""
    if string != '':
        return get_length(string[:-1]) + 1
    else:
        return 0


if '__main__' == __name__:
    data = input()
    print('Write down any integer')
    print(is_palindrome(data))
    print('Write down any string')
    print(get_length(data))
