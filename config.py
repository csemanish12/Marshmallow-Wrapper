import os

SQLALCHEMY_DATABASE_URI = F"postgresql://{os.environ.get('USER_NAME')}:" \
                          F"{os.environ.get('USER_PASSWORD')}@" \
                          F"{os.environ.get('HOST')}:" \
                          F"{os.environ.get('DATABASE_PORT')}/" \
                          F"{os.environ.get('DATABASE')}"
SECRET_KEY = "secret"
DEBUG = True