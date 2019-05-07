class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/blogdb'
    SECRET_KEY = "top secret"

    # Flask Security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'

