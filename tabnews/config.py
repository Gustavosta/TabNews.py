#!/usr/bin/python
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass(frozen=True, order=True, slots=True)
class Config:
    """
    Class that contains the configuration of the API.
    """

    HOST = "https://www.tabnews.com.br"
    TABNEWS_GITHUB_REPOSITORY = "filipedeschamps/tabnews.com.br"

    LOGIN_URL = HOST + "/api/v1/sessions"
    CONTENTS_URL = HOST + "/api/v1/contents"
    USER_DATA_URL = HOST + "/api/v1/user"
    USERS_DATA_URL = HOST + "/api/v1/users"
