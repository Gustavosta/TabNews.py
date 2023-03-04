#!/usr/bin/python
# -*- coding: utf-8 -*-

from json import decoder, dump, load, loads
from os.path import exists

from requests import post

from tabnews.config import Config
from tabnews.exceptions import InvalidCredentials, LoginRequired


def check_EH(email, host) -> tuple:
    return ({email: True}, {host: True})


class LoginMixin:
    def login(self):
        """
        Login to the TabNews API.

        Returns:
        --------
            dict | object: The user's data.
        """

        if self.email is None or self.password is None:
            raise LoginRequired(
                "É necessário informar o email e a senha do TabNews")

        url = Config.LOGIN_URL
        data = {
            "email": self.email,
            "password": self.password,
        }

        headers = {
            "Content-Type": "application/json",
        }

        response = post(url, json=data, headers=headers)
        if 200 <= response.status_code <= 201:
            self.session_id = response.json()["token"]
            self.logger.info("Logged in")

            return self.get_user()

        try:
            raise InvalidCredentials(
                f'{response.json()["message"]}\n{response.json()["action"]}\nStatus code: {response.status_code}')
        except KeyError:
            raise InvalidCredentials(
                "Credenciais inválidas ou ocorreu um erro no endpoint do TabNews")

    def load_config(self, use_preview_tabnews_host=False, path='config.json'):
        """
        Load the user's session id and configuration from a file.

        Args:
        -----
            use_preview_tabnews_host (bool): If True, the session id will be loaded from the preview tabnews host.
            path (str): The path to the file.

        Returns:
        --------
            str: The user's session id.
        """

        try:
            if self.config_path != path:
                self.config_path = path

            with open(path, 'r') as f:
                config = load(f)

                for session in config:
                    host = 'preview' if use_preview_tabnews_host else 'production'
                    value = check_EH(self.email, host)

                    if value[0] == session['email'] and value[1] == session['host']:
                        return session['session_id']

        except decoder.JSONDecodeError:
            print(
                "Arquivo de configuração inválido, verifique se o arquivo está no formato JSON")
            raise

        except FileNotFoundError:
            print("Arquivo de configuração não encontrado")
            raise

        except KeyError:
            print("Arquivo de configuração inválido")
            raise

    def dump_config(self, use_preview_tabnews_host=False, path='config.json'):
        """
        Save the user's session id and configuration to a file.

        Args:
        -----
            use_preview_tabnews_host (bool): If True, the session id will be saved to the preview tabnews host.
            path (str): The path to the file.
        """

        if self.config_path != path:
            self.config_path = path

        user_not_saved = True
        if not exists(path):
            with open(path, 'w') as f:
                pass

        with open(path, 'r+') as f:
            host = 'preview' if use_preview_tabnews_host else 'production'

            data = f.read()
            list_sessions = [] if data == '' else loads(data)

            value = check_EH(self.email, host)
            for session in list_sessions:
                if value[0][session['email']] and value[1][session['host']]:
                    user_not_saved = False
                    session['session_id'] = session

            if user_not_saved:
                list_sessions.append({
                    'session_id': self.session_id,
                    'email': self.email,
                    'host': host,
                })

            f.seek(0)

            dump(list_sessions, f, indent=4)
            f.truncate()



