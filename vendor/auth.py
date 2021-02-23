from configs.application import configs
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends
from configs.database import db
authConfig = configs['auth']
defaultAuth = authConfig[authConfig["default"]]
authDriver = defaultAuth['provider'][defaultAuth["driver"]]


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     disabled: Optional[bool] = None

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
    if authDriver["driver"] == "orm-query":
        return db.table(authDriver["table"]).where(key, ref).first()
    return 0

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

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, efaultAuth["secret_key"], algorithms=[defaultAuth["algorithm"]])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = getUser(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

print(defaultAuth)

