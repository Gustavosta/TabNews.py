#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging import getLogger


class ClientError(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
        self.logger = getLogger('TabNews')
        self.logger.error(f'\n{self.message}\n')


class LoginRequired(ClientError):
    def __init__(self, message):
        ClientError.__init__(self, message)


class InvalidCredentials(ClientError):
    def __init__(self, message):
        ClientError.__init__(self, message)


class InvalidTabnewsReturn(ClientError):
    def __init__(self, message):
        ClientError.__init__(self, message)


class BadTabnewsRequest(ClientError):
    def __init__(self, message):
        ClientError.__init__(self, message)


class BadUrl(ClientError):
    def __init__(self, message):
        ClientError.__init__(self, message)


class InsufficientTabcoins(ClientError):
    def __init__(self, message):
        ClientError.__init__(self, message)


class PreviewHostError(ClientError):
    def __init__(self, message):
        ClientError.__init__(self, message)


