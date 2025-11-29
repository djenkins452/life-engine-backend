from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    @staticmethod
    def hash_password(password: str):
        password = password[:72]       # Prevent bcrypt >72 byte crash
        return pwd_cxt.hash(password)

    @staticmethod
    def verify_password(plain: str, hashed: str):
        plain = plain[:72]
        return pwd_cxt.verify(plain, hashed)
