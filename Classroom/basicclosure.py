def outer_function(message):
    def inner_function():
        print(message)
        return inner_function
    
closure = outer_function("Hello World")
closure()