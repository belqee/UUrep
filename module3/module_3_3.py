def print_params(a=1, b='string', c=True) -> None:
    print(a, b, c)


if __name__ == '__main__':
    print_params()
    print_params(1, "2")
    print_params(1, "2", False)
    print()
    # works with warnings bc it was expected another types
    print_params("well")
    print_params(b=25)
    print_params(c=[1, 2, 3])
    print()

    values_list = [2, "2", False]
    values_dict = {'a': 3, 'b': "line", 'c': False}
    print_params(*values_dict)
    print_params(**values_dict)
    print()

    values_list_2 = ["1", 2]
    print_params(*values_list_2, 42)