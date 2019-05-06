class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/blogdb'
    SECRET_KEY = "top secret"

