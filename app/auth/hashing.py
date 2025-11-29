from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:

    @staticmethod
    def hash_password(password: str) -> str:
        # HARD LIMIT: bcrypt cannot handle >72 bytes
        if len(password.encode("utf-8")) > 72:
            raise ValueError("Password exceeds bcrypt's 72-byte limit.")

        return pwd_cxt.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        # Also truncate here before verifying
        if len(plain_password.encode("utf-8")) > 72:
            return False

        return pwd_cxt.verify(plain_password, hashed_password)
