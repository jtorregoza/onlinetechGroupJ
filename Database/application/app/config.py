from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):
    SQLALCHEMY_DATABASE_URI =
    'dialect+driver://username:password@host:port/database'