import os

""" Common config """
class Config(object):
    TESTING = False
    DEBUG = False


""" Development Config """
class DevelopmentConfig(Config):
    APP_ENV = "dev"
    SECRET_KEY = "60331c90-5dff-42d6-ba65-161c7abaf879"
    MYDB = "db.json"


""" Staging Config """
class StagingConfig(Config):
    APP_ENV = "staging"


""" Production Config """
class ProductionConfig(Config):
    APP_ENV = "prod"



""" 
    method: get_config 
    environment variable: APP_ENV
    values:
        - dev
        - staging
        - prod
"""
def get_config():
    config_env = os.environ.get("APP_ENV", "dev")

    if config_env == "dev":
        return DevelopmentConfig
    elif config_env == "staging":
        return StagingConfig
    elif config_env == "prod":
        return ProductionConfig
    else:
        raise ValueError("invalid config envoironment: ", config_env)