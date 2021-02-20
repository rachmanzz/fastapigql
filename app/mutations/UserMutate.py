import graphene
from models.user import User
from app.serializers.UserSerialize import UserGrapheneModel, UserGrapheneInputModel

class CreateUser(graphene.Mutation):
    class Arguments:
        user_details = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_details):
        user = User()
        if 'username' in user_details:
            user.username = user_details.username
        user.email = user_details.email
        user.password = user_details.password
        user.status = "guest"
        user.save()
        return user