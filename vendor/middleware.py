from typing import Optional
def decorators(func):
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)
    return wrap
def customMiddleware(middleware, func=decorators):
    def wrap(*args, **kwargs):
        return middleware(*args,next=func, **kwargs)
    return wrap