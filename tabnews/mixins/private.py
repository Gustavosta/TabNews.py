from tabnews.utils import tabnews_return_validator

import requests


class PrivateRequestMixin:
    def get_headers(self):
        """
        Get the headers to be used in the requests.
        
        Returns:
        --------
            dict: The headers to be used in the requests.
        """

        return {
            "Content-Type": "application/json",
            "Cookie": f"session_id={self.session_id}",
        }

    def get(self, url, data=None):
        """
        Make a GET request to the TabNews API.
        
        Args:
        -----
            url (str): The URL to be searched for.
            data (dict): The data to be sent in the request.
            
        Returns:
        --------
            dict | object: The data of the URL.
        """
        
        headers = self.get_headers()
        return tabnews_return_validator(requests.get(url, headers=headers, json=data))

    def post(self, url, data):
        """
        Make a POST request to the TabNews API.
        
        Args:
        -----
            url (str): The URL to be searched for.
            data (dict): The data to be sent in the request.
            
        Returns:
        --------
            dict | object: The data of the URL.
        """
        
        headers = self.get_headers()
        return tabnews_return_validator(requests.post(url, headers=headers, json=data))
    
    def patch(self, url, data):
        """
        Make a PATCH request to the TabNews API.
        
        Args:
        -----
            url (str): The URL to be searched for.
            data (dict): The data to be sent in the request.
            
        Returns:
        --------
            dict | object: The data of the URL.
        """
        
        headers = self.get_headers()
        return tabnews_return_validator(requests.patch(url, headers=headers, json=data))