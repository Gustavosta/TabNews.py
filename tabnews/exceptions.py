import logging


class ClientError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.logger = logging.getLogger('TabNews')
        self.logger.error(f'\nError: {self.message}\n')


class LoginRequired(ClientError):
    status_code = 401

    def __init__(self, message, status_code=None, payload=None):
        ClientError.__init__(self, message, status_code, payload)
    

class InvalidCredentials(ClientError):
    status_code = 401

    def __init__(self, message, status_code=None, payload=None):
        ClientError.__init__(self, message, status_code, payload)


