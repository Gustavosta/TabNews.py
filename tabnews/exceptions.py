import logging


class ClientError(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
        self.logger = logging.getLogger('TabNews')
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



