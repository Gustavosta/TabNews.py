import requests

from tabnews.exceptions import InvalidCredentials, LoginRequired
from tabnews.config import Config


class LoginMixin:
    session_id = None
    
    def login(self):
        if self.email is None or self.password is None:
            raise LoginRequired("É necessário informar o email e a senha do TabNews")

        url = Config.LOGIN_URL
        data = {
            "email": self.email,
            "password": self.password,
        }
        print(data)

        headers = {
            "Content-Type": "application/json",
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.text)
        if response.status_code == 200 or response.status_code == 201:
            self.session_id = response.json()["token"]
            self.logger.info("Logged in")
        else:
            try:
                raise InvalidCredentials(f'{response.json()["message"]}\n{response.json()["action"]}\nStatus code: {response.status_code}')
            except KeyError:
                raise InvalidCredentials("Credenciais inválidas ou ocorreu um erro no endpoint do TabNews")


