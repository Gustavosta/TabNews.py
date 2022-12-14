from tabnews.exceptions import InvalidTabnewsReturn

import json


def is_json_return(response):
    try:
        json.loads(response.text)
    except ValueError:
        raise InvalidTabnewsReturn('O retorno da requisição não é um JSON válido, verifique o status de funcionamento do TabNews.')
    return response



