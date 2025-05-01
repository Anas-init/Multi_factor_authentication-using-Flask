from decouple import config
import datetime

DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default="guess-me")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    APP_NAME = config("APP_NAME")
    
    # JWT Configuration
    JWT_SECRET_KEY = config("JWT_SECRET_KEY", default="super-jwt-secret")
    JWT_TOKEN_LOCATION = ['cookies']  # Store JWT in cookies for template-based app
    JWT_COOKIE_CSRF_PROTECT = True  # Enable CSRF protection for cookies
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(
        seconds=config("JWT_ACCESS_EXPIRATION_SECONDS", default=3600, cast=int)  # 1 hour default
    )
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(
        days=config("JWT_REFRESH_EXPIRATION_DAYS", default=30, cast=int)  # 30 days default
    )
    JWT_COOKIE_SECURE = False  # Set to True in production
    JWT_CSRF_IN_COOKIES = True  # Store CSRF token in cookies
    JWT_CSRF_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE']  # Methods that require CSRF protection


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = config('WTF_CSRF_ENABLED', default=False, cast=bool)
    DEBUG_TB_ENABLED = config('DEBUG_TB_ENABLED', default=True, cast=bool)
    # For development, you can use shorter token expiration
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
    JWT_COOKIE_SECURE = False  # Allow non-HTTPS in development


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    # For testing, use very short expiration
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=30)
    JWT_COOKIE_SECURE = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False
    JWT_COOKIE_SECURE = True  
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(
        seconds=config("JWT_ACCESS_EXPIRATION_SECONDS", default=3600, cast=int)
    )