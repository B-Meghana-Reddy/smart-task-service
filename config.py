import os

class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://taskuser:Task123@localhost/taskdb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False