from tabnews.utils import is_json_return

import requests


class PrivateRequestMixin:
    session_id = None

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Cookie": f"session_id={self.session_id}",
        }

    def get(self, url, data=None):
        headers = self.get_headers()
        return is_json_return(requests.get(url, headers=headers, json=data))

    def post(self, url, data):
        headers = self.get_headers()
        return is_json_return(requests.post(url, headers=headers, json=data))



