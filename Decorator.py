def decorator_text_uppercase(func):
    def wrapper():
        function = func()
        text_uppercase = function.upper()
        return text_uppercase
    return wrapper

def text():
    return 'EduaRd SiNaGa'
decorated_result = decorator_text_uppercase(text)
print(decorated_result())

@decorator_text_uppercase
def text():
    return 'EduaRd SinaGa'
print(text())

def do_twice(function):
    def wrapper_do_twice():
        function()
        function()
    return wrapper_do_twice
@do_twice
def text():
    print('EduaRd SinaGa')
text()
