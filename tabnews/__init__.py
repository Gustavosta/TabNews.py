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

    def __init__(self, email=None, password=None, logger=DEFAULT_LOGGER):
        self.email = email or os.environ.get('TABNEWS_EMAIL')
        self.password = password or os.environ.get('TABNEWS_PASSWORD')
        self.logger = logger

        self.login()


