import graphene
from app.mutations.UserMutate import CreateUser, DelateUser, UserLogin

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DelateUser.Field()
    user_login = UserLogin.Field()


