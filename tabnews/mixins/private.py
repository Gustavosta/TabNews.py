from tabnews.utils import tabnews_return_validator

import requests


class PrivateRequestMixin:
    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Cookie": f"session_id={self.session_id}",
        }

    def get(self, url, data=None):
        headers = self.get_headers()
        return tabnews_return_validator(requests.get(url, headers=headers, json=data))

    def post(self, url, data):
        headers = self.get_headers()
        return tabnews_return_validator(requests.post(url, headers=headers, json=data))
    
    def patch(self, url, data):
        headers = self.get_headers()
        return tabnews_return_validator(requests.patch(url, headers=headers, json=data))

