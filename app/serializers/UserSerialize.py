from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel
from app.serializers.AccountSerialize import AccountModel


class UserModel(BaseModel):
    id: int
    username: Optional[str]
    email: str
    status: str
    is_active: bool
    password: str
    account: Optional[AccountModel]


class UserGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('id', 'account', 'status', 'is_active')

class UserGrapheneModel(PydanticObjectType):
    class Meta:
        model = UserModel
        xclude_fields = ('password', 'account')
