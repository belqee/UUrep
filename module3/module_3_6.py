def calculate_structure_sum(data_structure):
    if isinstance(data_structure, (int, float, bool)):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        count = 0
        for item in data_structure:
            count += calculate_structure_sum(item)
        return count
    elif isinstance(data_structure, dict):
        count = 0
        for key, value in data_structure.items():
            count += calculate_structure_sum(key) + calculate_structure_sum(value)
        return count
    return 0

if __name__ == '__main__':
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
    print(calculate_structure_sum(data_structure))
