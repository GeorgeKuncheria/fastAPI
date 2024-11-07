from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hashing passwords
class Hash:
    def bcrypt( password : str):
        return pwd_context.hash(password)

