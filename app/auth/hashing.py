from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    @staticmethod
    def hash_password(password: str):
        # ensure bcrypt-safe
        password = password[:72]
        return pwd_cxt.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        plain_password = plain_password[:72]
        return pwd_cxt.verify(plain_password, hashed_password)
