import pydantic
from typing import Optional

class AuthBase(pydantic.BaseModel):
    user_id: int
    username: Optional[str]
    email: Optional[str]
