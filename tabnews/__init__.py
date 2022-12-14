from tabnews.mixins.auth import LoginMixin
from tabnews.mixins.private import PrivateRequestMixin
from tabnews.mixins.account import GetUserMixin

import logging, os


DEFAULT_LOGGER = logging.getLogger('TabNews')


class Client(
    LoginMixin,
    PrivateRequestMixin,
    GetUserMixin,
):

    def __init__(self, email=None, password=None, save_session=True, config_path='config.json', logger=DEFAULT_LOGGER):
        self.email = email or os.environ.get('TABNEWS_EMAIL')
        self.password = password or os.environ.get('TABNEWS_PASSWORD')
        self.logger = logger
        self.config_path = config_path

        if save_session == True:
            if os.path.exists(self.config_path):
                self.session_id = self.load_config()
                self.logger.info("Session loaded")
            else:
                self.login()
                self.dump_config()
                self.logger.info("Session saved")
        else:
            self.login()


