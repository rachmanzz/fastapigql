import graphene
from vendor.middleware import customMiddleware

def checkUser(*args, next, **kwargs):
    print(args)
    print(kwargs)
    return next(*args, **kwargs)


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))

    @customMiddleware(middleware=checkUser)
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'