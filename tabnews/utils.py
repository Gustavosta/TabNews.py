from tabnews.exceptions import InvalidTabnewsReturn, BadTabnewsRequest, PreviewHostError
from tabnews.config import Config

from cleverdict import CleverDict
import json, re, requests


def get_preview_url():
    try:
        url = F'https://api.github.com/repos/{Config.TABNEWS_GITHUB_REPOSITORY}/deployments'
        response = requests.get(url).json()
        id = None
        
        for deployment in response:
            if deployment['environment'].lower() == 'preview':
                id = deployment['id']
                break
            
        if id is None:
            raise ValueError('No deployment found')
        
        else:
            url = f'https://api.github.com/repos/{Config.TABNEWS_GITHUB_REPOSITORY}/deployments/{id}/statuses'
            response = requests.get(url).json()
            
            for status in response:
                if status['state'] == 'success':
                    return status['target_url']
                
    except:
        raise PreviewHostError('Não foi possível obter o host do homologação do Tabnews.')


def url_validator(url):
    regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    return True if re.search(regex, url) else False


def dict_and_object(dictonary):
    if type(dictonary) == dict:
        return CleverDict(dictonary)
    return dictonary


def tabnews_return_validator(response):
    try:
        if type(response) != str and type(response) != dict:
            response = response.text

        json_loaded = json.loads(response)

        if 'action' in json_loaded:
            raise BadTabnewsRequest(f'Bad request: {json_loaded["message"]}\n{json_loaded["action"]}')
        return dict_and_object(json_loaded)

    except ValueError:
        raise InvalidTabnewsReturn('O retorno da requisição não é um JSON válido, verifique o status de funcionamento do TabNews.')


