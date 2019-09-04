class Config():
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://adesupraptolaia:alta123@localhost/ecommerce'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://adesupraptolaia:alta123@localhost/ecommerce_test'