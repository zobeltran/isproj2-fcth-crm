"""
This is the Configuration
"""


class BaseConfig(object):
    """ This is the main config class to be inherited """
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """ This is the main configuration class """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\Renzo\Documents\Codes\Python\isproj2-fcth-crm\dev\crm.db'
    SECRET_KEY = 'developmentsecretkey'
    UPLOAD_FOLDER = 'app/upload'
    USER_ENABLE_EMAIL = False


class ProductionConfig(BaseConfig):
    """ This is the production configuration class """
    DATABASE = ''.join(['postgresql://zccisfiglvdagd:',
                        '5d5fe904f02e350ca33066c2a51a5c6cc0c5236ade95b403cea2418d0ca567c2',
                        '@ec2-54-243-255-57.compute-1.amazonaws.com:5432/dfn8ta0mogh2u9'])
    SECRET_KEY = '\xd6;\x9aq)\xea\xa5\x9c\xf5BM^N\x05X\\\xec5w\x0f\xb9\xab\xf9\xb8'
    UPLOAD_FOLDER = 'app/upload'
    SQLALCHEMY_DATABASE_URI = DATABASE
    USER_ENABLE_EMAIL = False
