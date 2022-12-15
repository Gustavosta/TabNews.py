import requests, json

from tabnews.exceptions import InvalidCredentials, LoginRequired
from tabnews.config import Config


class LoginMixin:
    def login(self):
        if self.email is None or self.password is None:
            raise LoginRequired("É necessário informar o email e a senha do TabNews")

        url = Config.LOGIN_URL
        data = {
            "email": self.email,
            "password": self.password,
        }

        headers = {
            "Content-Type": "application/json",
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            self.session_id = response.json()["token"]
            self.logger.info("Logged in")

        else:
            try:
                raise InvalidCredentials(f'{response.json()["message"]}\n{response.json()["action"]}\nStatus code: {response.status_code}')
            except KeyError:
                raise InvalidCredentials("Credenciais inválidas ou ocorreu um erro no endpoint do TabNews")


    def load_config(self, path='config.json'):
        try:
            if self.config_path != path:
                self.config_path = path

            with open(path, 'r') as f:
                config = json.load(f)
                session_id = config.get('session_id')
                return session_id

        except json.decoder.JSONDecodeError:
            raise json.decoder.JSONDecodeError("Arquivo de configuração inválido, verifique se o arquivo está no formato JSON")

        except FileNotFoundError:
            raise FileNotFoundError("Arquivo de configuração não encontrado")

        except KeyError:
            raise KeyError("Arquivo de configuração inválido")


    def dump_config(self, path='config.json'):
        try:
            if self.config_path != path:
                self.config_path = path

            with open(path, 'w') as f:
                config = {
                    'session_id': self.session_id,
                }
                json.dump(config, f)
            
        except Exception as e:
            raise e



