import graphene
from app.mutations.UserMutate import CreateUser, DelateUser

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DelateUser.Field()


