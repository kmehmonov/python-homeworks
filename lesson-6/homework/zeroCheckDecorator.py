
# method-1
def check(func):
    """
    Check for ZeroDivisionError
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Denominator can't be zero")
            return None
    return wrapper

# method-2
def check2(func):
    """
    Check for ZeroDivisionError
    """
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            print("Denominator can't be zero")
            return None
        else:
            return func(*args, **kwargs)
    return wrapper



@check              # method-1
# @check2           # method-2
def div(a, b):
    return a / b

a = div(4, 0)
print(a)

   
