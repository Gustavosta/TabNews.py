#!/usr/bin/python
# -*- coding: utf-8 -*-

import httpx

from tabnews.utils import tabnews_return_validator


class PrivateRequestMixin:
    def __init__(self) -> None:
        self.__client = httpx.Client()

    def __headers(self):
        return self.get_headers()

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

    def get(self, url):
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

        return tabnews_return_validator(
            self.__client.get(url, headers=self.__headers())
        )

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

        return tabnews_return_validator(
            self.__client.post(url, headers=self.__headers(), json=data)
        )

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

        return tabnews_return_validator(
            self.__client.patch(url, headers=self.__headers(), json=data)
        )
