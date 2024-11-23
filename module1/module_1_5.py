immutable_var = (1,5.5,[1,2,3],(4,5,6))
print(immutable_var)

#immutable_var[0] = 1 #нельзя т.к. класс неизменяемый

mutable_list = [1,2,3]
mutable_list[1] = 3
print(mutable_list)