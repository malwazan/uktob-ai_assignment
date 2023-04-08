

""" import api """
from app import create_app
from config import get_config


""" create app """
app = create_app(get_config())


""" serve locally """
if __name__ == '__main__':
    app.run()