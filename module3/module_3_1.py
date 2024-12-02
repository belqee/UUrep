from typing import List, Tuple

calls = 0

def count_calls() -> None:
    global calls
    calls += 1
    return

def string_info(string : str) -> Tuple[int, str, str]:
    count_calls()
    return len(string), str.upper(string), str.lower(string)

def is_contains(string: str, list_to_search: List[str]) -> bool:
    count_calls()
    for i in list_to_search:
        i = str.lower(i)
        if i == str.lower(string):
            return True
    return False

if __name__ == '__main__':
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
    print(is_contains('cycle', ['recycling', 'cyclic']))
    print(calls)