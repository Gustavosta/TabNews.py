#!/usr/bin/python
# -*- coding: utf-8 -*-

from json import loads
from re import search

import requests
from cleverdict import CleverDict

from tabnews.config import Config
from tabnews.exceptions import (BadTabnewsRequest, InvalidTabnewsReturn,
                                PreviewHostError)


def get_preview_url():
    """
    Get the preview URL on GitHub repository of the Tabnews.

    Returns:
    --------
        str: The preview URL of the Tabnews.
    """

    try:
        url = F'https://api.github.com/repos/{Config.TABNEWS_GITHUB_REPOSITORY}/deployments'
        response = requests.get(url).json()
        value = [{'preview': True}, {'success': True}]

        id = (*(
            deployment['id']
            for deployment in response
            if deployment['environment'].lower() in value[0]
        ),)[-1]

        if id is None:
            raise ValueError('No deployment found')

        url = f'https://api.github.com/repos/{Config.TABNEWS_GITHUB_REPOSITORY}/deployments/{id}/statuses'
        response = requests.get(url).json()

        for status in response:
            return status['target_url']
            """
            if value[0][status['state']]:
                return status['target_url']
            """

    except PreviewHostError:
        print('Não foi possível obter o host do homologação do Tabnews.')
        raise


def url_validator(url):
    """
    Validate the URL.

    Args:
    -----
        url (str): The URL to be validated.

    Returns:
    --------
        bool: True if the URL is valid, False otherwise.
    """

    regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    return True if search(regex, url) else False


def dict_and_object(dictonary):
    """
    Convert a dict to a CleverDict object.
    """

    if type(dictonary) == dict:
        return CleverDict(dictonary)
    return dictonary


def tabnews_return_validator(response):
    """
    Validate the return of the Tabnews API.

    Args:
    -----
        response (str | dict): The response of the Tabnews API.

    Returns:
    --------
        dict | object: The response of the Tabnews API.
    """

    try:
        if type(response) != str and type(response) != dict:
            response = response.text

        json_loaded = loads(response)

        if 'action' in json_loaded:
            raise BadTabnewsRequest(
                f'Bad request: {json_loaded["message"]}\n{json_loaded["action"]}')

        return dict_and_object(json_loaded)

    except ValueError:
        raise InvalidTabnewsReturn(
            'O retorno da requisição não é um JSON válido, verifique o status de funcionamento do TabNews.')
