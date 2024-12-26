def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

#inner_function() #не скомпилируется (или правильно сказать не интерпретируется??) т.к. эта функция находится внутри локальной области функции test_function()
test_function() # проблем нет