#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging import getLogger
from os import environ
from os.path import exists

from tabnews.config import Config
from tabnews.mixins.account import GetUserMixin
from tabnews.mixins.auth import LoginMixin
from tabnews.mixins.comments import CommentMixin
from tabnews.mixins.posts import PostMixin
from tabnews.mixins.private import PrivateRequestMixin
from tabnews.mixins.tabcoins import TabcoinsMixin
from tabnews.utils import get_preview_url


DEFAULT_LOGGER = getLogger('TabNews')


class Client(
    LoginMixin,
    PrivateRequestMixin,
    GetUserMixin,
    PostMixin,
    TabcoinsMixin,
    CommentMixin,
):
    """The TabNews client."""

    def __init__(
        self, email=None, password=None, token=None,
        save_session=True, config_path='config.json',
        use_preview_tabnews_host=False, logger=DEFAULT_LOGGER
    ) -> None:

        self.email = email or environ.get('TABNEWS_EMAIL')
        self.password = password or environ.get('TABNEWS_PASSWORD')
        self.logger = logger
        self.config_path = config_path

        if use_preview_tabnews_host:
            new_host = get_preview_url()
            atual_host = Config.HOST
            self.logger.info(f"Usando o ambiente de homologação: {new_host}")

            for key, value in Config.__dict__.items():
                if isinstance(value, str):
                    setattr(Config, key, value.replace(atual_host, new_host))

        if token is not None:
            self.session_id = token

        elif save_session:
            if exists(self.config_path):
                self.session_id = self.load_config(use_preview_tabnews_host)

                if self.session_id is None:
                    self.enter_session(
                        use_preview_tabnews_host, 'Session loaded')

            else:
                self.enter_session(
                    use_preview_tabnews_host, 'Session saved')

        else:
            self.login()

    def enter_session(self, use_preview_tabnews_host, info):
        self.login()
        self.dump_config(use_preview_tabnews_host)
        self.logger.info(info)


