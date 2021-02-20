from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel

class AccountModel(BaseModel):
    id: int
    user_id: int
    balance: int

class AccountGrapheneModel(PydanticObjectType):
    class Meta:
        model = AccountModel
        xclude_fields = ('user_id')

class AccountGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = AccountModel
        exclude_fields = ('id')