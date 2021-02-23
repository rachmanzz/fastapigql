import graphene
from models.user import User
from app.serializers.UserSerialize import UserGrapheneModel, UserGrapheneInputModel
from vendor.auth import hashing_password
class CreateUser(graphene.Mutation):
    class Arguments:
        user_details = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_details):
        try:
            user = User()
            if 'username' in user_details:
                user.username = user_details.username
            user.email = user_details.email
            user.password = hashing_password(user_details.password)
            user.status = "guest"
            user.save()
            return user
        except:
            return UserGrapheneModel(username=None, email="rachman.sd@gmail.com")


class DeleteUserInput(graphene.InputObjectType):
    id = graphene.Int()

class UserStatus(graphene.ObjectType):
    ok = graphene.Boolean()

class DelateUser(graphene.Mutation):
    class Arguments:
        input = graphene.Int()

    Output = UserStatus

    @staticmethod
    def mutate(parent, info, input):
        try:
            user = User.find_or_fail(input)
            user.delete()
            UserStatus(ok=True)
        except:
            return UserStatus(ok=False)
