from functools import wraps


def cmp_dec_1(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if args[0] < args[1]:
            raise RuntimeError
        else:
            print(f'{args[0]} : {args[1]}')
        return f(*args, **kwargs)

    return decorated_func


def cmp_dec_2(n: int):
    def inner_func(f):
        @wraps(f)
        def decorated_func(*args, **kwargs):
            if args[0] < n:
                raise RuntimeError
            else:
                print(f'{args[0]} : {args[1]}')
            return f(*args, **kwargs)

        return decorated_func

    return inner_func


class obj1:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class obj2:
    def __init__(self, a, b):
        self.a = a
        self.b = b


@cmp_dec_1
def abs1(a, b):
    return a + b


@cmp_dec_2(3)
def abs2(a, b):
    return a + b


def test(*args, **kwargs):
    print(args)
    print(kwargs)


o1 = obj1(2, 3)
o2 = obj2(5, 6)
test(o1, o2)

abs1(3, 2)
abs2(4, 2)
