from configs.application import configs
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, utils
from passlib.context import CryptContext
from jose import ExpiredSignatureError, jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, Request
from configs.database import db
from app.Auth import AuthBase
from graphql import GraphQLError
authConfig = configs['auth']
defaultAuth = authConfig[authConfig["default"]]
authDriver = defaultAuth['provider'][defaultAuth["driver"]]


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserNotFound(Exception):
    pass

class UnkownJWTModel(Exception):
    pass


class TokenData(BaseModel):
    username: Optional[str] = None

def hashed_verify(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except:
        return False


def hashing_password(password):
    return pwd_context.hash(password)


def getUser(key, ref):
    try: 
        return db.table(authDriver["table"]).where(key, ref).first()
    except:
        return None

def getUserById(user_id: int):
    try: 
        return db.table(authDriver["table"]).where("id", user_id).first()
    except:
        return None

def authenticate_user(refer: str, password_plain: str, key: str = "email"):
    user = getUser(key, refer)
    if not user:
        return False
    if not hashed_verify(password_plain, user["password"]):
        return False
    return user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, defaultAuth["secret_key"], algorithm=defaultAuth["algorithm"])
    return encoded_jwt

async def get_current_user(request: Request) -> Optional[AuthBase]:
    authorization: str = request.headers.get("Authorization")
    if not authorization:
        return None
    _, token = authorization.split(" ")
    try:
        payload = jwt.decode(token, defaultAuth["secret_key"], algorithms=[defaultAuth["algorithm"]])
        getUser = payload.get("user")
        if getUser is None:
            raise UnkownJWTModel()
        user = getUserById(getUser["user_id"])
        if not user:
            raise UserNotFound()
        return AuthBase(**{"user_id": user.id, "username": user.username, "email": user.email})
    except ExpiredSignatureError as error:
        raise HTTPException(status_code=401, detail="Signature has expired")
    except JWTError as error:
        raise HTTPException(status_code=401, detail="Signature invalid")
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")
    except UnkownJWTModel:
        raise HTTPException(status_code=401, detail="Unkown signature model")
    except:
        raise HTTPException(status_code=404, detail="Unkown Error")


def authenticate_require(func):
    def wrap(*args, **kwargs):
        _, info = args
        if "request" in info.context and info.context["request"].state.current_user:
            user = info.context["request"].state.current_user
            kwargs["user"] = user
            return func(*args, **kwargs)
        raise GraphQLError('authenticate required')
    return wrap

