from passlib.context import CryptContext

# Configure Passlib to use only bcrypt
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    @staticmethod
    def hash_password(password: str):
        """
        Hash a plain password using bcrypt.
        """
        return pwd_cxt.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        """
        Verify a plain password against a hashed password.
        """
        return pwd_cxt.verify(plain_password, hashed_password)
