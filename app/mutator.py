import graphene
from app.mutations.UserMutate import CreateUser

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


