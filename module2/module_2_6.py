def calculate_code(n):
    result = ''
    for i in range(1,n//2 + 1):
        for j in range(i + 1,n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

#print(*[calculate_code(n) for n in range(3, 21)],sep='\n')
print(calculate_code(int(input('Введите число'))))