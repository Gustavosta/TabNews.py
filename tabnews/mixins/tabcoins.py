#!/usr/bin/python
# -*- coding: utf-8 -*-

from tabnews.config import Config
from tabnews.exceptions import InsufficientTabcoins


class TabcoinsMixin:
    @staticmethod
    def __URL(username, slug_or_parent_id):
        return (
            Config.CONTENTS_URL + "/" + username + "/" + slug_or_parent_id + "/tabcoins"
        )

    def upvote(self, username, slug_or_parent_id, upvote_amount=1):
        """
        Upvote a content.

        Args:
        -----
            username (str): The username of the content's author.
            slug_or_parent_id (str): The slug or parent_id of the content.
            upvote_amount (int): The amount of upvotes to be given.

        Returns:
        --------
            dict | object: The content's data.
        """

        tabcoins_limit = self.get_user()["tabcoins"]
        url = self.__URL(username, slug_or_parent_id)
        data = {"transaction_type": "credit"}

        return self.result_check(upvote_amount, tabcoins_limit, url, data)

    def downvote(self, username, slug_or_parent_id, downvote_amount=1):
        """
        Downvote a content.

        Args:
        -----
            username (str): The username of the content's author.
            slug_or_parent_id (str): The slug or parent_id of the content.
            upvote_amount (int): The amount of upvotes to be given.

        Returns:
        --------
            dict | object: The content's data.
        """

        tabcoins_limit = self.get_user()["tabcoins"]
        url = self.__URL(username, slug_or_parent_id)
        data = {"transaction_type": "debit"}

        return self.result_check(downvote_amount, tabcoins_limit, url, data)

    def result_check(self, _amount, tabcoins_limit, url, data) -> dict:
        if _amount * 2 > tabcoins_limit:
            raise InsufficientTabcoins(
                f"Você não possui tabcoins suficientes para realizar essa ação!\nVocê possui {tabcoins_limit} tabcoins, mas precisa de {_amount*2} para realizar essa ação."
            )

        result = {"tabcoins": None}
        for i in range(_amount):
            result = self.post(url, data)

        return result
