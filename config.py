import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASS = os.getenv("MONGO_PASS")
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_URI = (
        f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@database.iirfppa.mongodb.net/"
        f"{MONGO_DB}?retryWrites=true&w=majority&appName=Database"
    )
