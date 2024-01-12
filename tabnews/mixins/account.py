#!/usr/bin/python
# -*- coding: utf-8 -*-

from tabnews.config import Config


class GetUserMixin:
    def get_user(self, username=None):
        """
        Get the user's data or the data of a specific user.

        Args:
        -----
            username (str): The username of the user to be searched for.

        Returns:
        --------
            dict | object: The user's data or the data of a specific user.
        """

        if username is None:
            url = Config.USER_DATA_URL
            return self.get(url)

        url = Config.USERS_DATA_URL + f"/{username}"

        response = self.get(url)

        return response
