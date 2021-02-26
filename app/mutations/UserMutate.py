import graphene
from models.user import User
from app.serializers.UserSerialize import UserGrapheneModel, UserGrapheneInputModel
from vendor.auth import hashing_password, authenticate_user, create_access_token
from typing import Optional
from pydantic import BaseModel
from app.Auth import AuthBase

class UserInfo(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None

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

class UserLoginStatus(graphene.ObjectType):
    token = graphene.String()
    status = graphene.Boolean()


class UserLogin(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()
    Output = UserLoginStatus

    @staticmethod
    def mutate(parent, info, email, password):
        user = authenticate_user(email, password)
        if not user:
            print("there not user")
            return UserLoginStatus(token="", status=False)
        token = create_access_token({"user": {"user_id": user.id}})
        return UserLoginStatus(token=token, status=False)
    

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
