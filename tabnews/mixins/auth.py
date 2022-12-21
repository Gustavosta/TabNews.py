#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json, os

from tabnews.exceptions import InvalidCredentials, LoginRequired
from tabnews.config import Config


class LoginMixin:
    def login(self):
        """
        Login to the TabNews API.
        
        Returns:
        --------
            dict | object: The user's data.
        """
        
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
            return self.get_user()

        else:
            try:
                raise InvalidCredentials(f'{response.json()["message"]}\n{response.json()["action"]}\nStatus code: {response.status_code}')
            except KeyError:
                raise InvalidCredentials("Credenciais inválidas ou ocorreu um erro no endpoint do TabNews")


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
                config = json.load(f)
                for session in config:
                    host = 'production'
                    if use_preview_tabnews_host == True:
                        host = 'preview'
                    if session['email'] == self.email and session['host'] == host:
                        self.session_id = session['session_id']
                        return self.session_id

        except json.decoder.JSONDecodeError:
            raise json.decoder.JSONDecodeError("Arquivo de configuração inválido, verifique se o arquivo está no formato JSON")

        except FileNotFoundError:
            raise FileNotFoundError("Arquivo de configuração não encontrado")

        except KeyError:
            raise KeyError("Arquivo de configuração inválido")


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
        if not os.path.exists(path):
            with open(path, 'w') as f:
                pass
            
        with open(path, 'r+') as f:
            host = 'production'
            if use_preview_tabnews_host == True:
                host = 'preview'
                
            data = f.read()
            if data == '':
                list_sessions = []
            else:
                list_sessions = json.loads(data)
            
            for session in list_sessions:
                if session['email'] == self.email and session['host'] == host:
                    user_not_saved = False
                    session['session_id'] = session

            if user_not_saved:
                list_sessions.append({
                    'session_id': self.session_id,
                    'email': self.email,
                    'host': host,
                })

            f.seek(0)
            
            json.dump(list_sessions, f, indent=4)
            f.truncate()

