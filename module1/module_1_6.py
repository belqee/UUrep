my_dict = { 'Alex': 1999, 'Petya': 2003, 'Vasya':2004, 'Misha': 1997}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Ivan'))
my_dict.update({'Ivan': 2005, 'Vlad': 2000})
print(my_dict.pop('Petya'))
print(my_dict, '\n')

my_set = {1, 'string', 5.5, 'hello', 1}
print(my_set)
my_set.update({2,3})
my_set.remove('string')
print(my_set)