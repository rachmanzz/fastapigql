import graphene
from vendor.auth import authenticate_require

class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))

    @authenticate_require
    def resolve_say_hello(parent, info, name, user):
        return f'Hello {name}'