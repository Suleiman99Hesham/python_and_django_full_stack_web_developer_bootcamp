def new_decorator(func):
    def wrap_func():
        print("SOME CODE BEFORE EXECUTING FUNCTION!")
        func()
        print("FUNC() HAS BEEN EXECUTED")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()