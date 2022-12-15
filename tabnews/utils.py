from tabnews.exceptions import InvalidTabnewsReturn, BadTabnewsRequest

import json, re


def url_validator(url):
    regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    return True if re.search(regex, url) else False


def tabnews_return_validator(response):
    try:
        #print(f'\n{response.text}\n')
        if type(response) != str and type(response) != dict:
            response = response.text

        json_loaded = json.loads(response)

        if 'action' in json_loaded:
            raise BadTabnewsRequest(f'Bad request: {json_loaded["message"]}\n{json_loaded["action"]}')
        return json_loaded

    except ValueError:
        raise InvalidTabnewsReturn('O retorno da requisição não é um JSON válido, verifique o status de funcionamento do TabNews.')

