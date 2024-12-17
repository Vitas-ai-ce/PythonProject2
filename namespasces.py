# Урок "Пространства имен и области видимости"

# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function,
# Эта функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function():
    def inner_function():
        d = 'Я в области видимости функции test_function'
        print(d)

    return inner_function()


test_function()
# inner_function() # результат NameError
