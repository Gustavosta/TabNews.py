#!/usr/bin/python
# -*- coding: utf-8 -*-

from tabnews.config import Config
from tabnews.exceptions import BadUrl
from tabnews.utils import url_validator


class PostMixin:
    @staticmethod
    def URL(s):
        return Config.CONTENTS_URL + f"?strategy={s}"

    def get_post(self, username, slug):
        """
        Get a specific content.

        Args:
        -----
            username (str): The username of the content's author.
            slug (str): The slug of the content.

        Returns:
        --------
            dict | object: The content's data.
        """

        return self.get(Config.CONTENTS_URL + "/" + username + "/" + slug)

    def list_posts_from_url(self, url, all_posts=False):
        """
        List the contents of a specific URL.

        Args:
        -----
            url (str): The URL to be searched for.
            all_posts (bool): If True, all the contents of the URL will be returned.

        Returns:
        --------
            list: The contents of a specific URL.
        """

        posts = []
        page = 1

        while 1:
            prefix = "&" if "?" in url else "?"

            data = self.get(url + f"{prefix}page={page}")
            if not data:
                break

            posts.extend(data)
            if not all_posts:
                break

            page += 1
        return posts

    def get_posts_from_user(self, username, all_posts=False):
        """
        Get the contents of a specific user.

        Args:
        -----
            url (str): The URL to be searched for.
            all_posts (bool): If True, all the contents of the URL will be returned.

        Returns:
        --------
            list: The contents of a specific URL.
        """

        return self.list_posts_from_url(Config.CONTENTS_URL + "/" + username, all_posts)

    def get_relevant_posts(self, all_posts=False):
        """
        Get the relevant contents.

        Args:
        -----
            url (str): The URL to be searched for.
            all_posts (bool): If True, all the contents of the URL will be returned.

        Returns:
        --------
            list: The contents of a specific URL.
        """

        return self.list_posts_from_url(self.URL("relevant"), all_posts)

    def get_new_posts(self, all_posts=False):
        """
        Get the new contents.

        Args:
        -----
            url (str): The URL to be searched for.
            all_posts (bool): If True, all the contents of the URL will be returned.

        Returns:
        --------
            list: The contents of a specific URL.
        """

        return self.list_posts_from_url(self.URL("new"), all_posts)

    def get_old_posts(self, all_posts=False):
        """
        Get the old contents.

        Args:
        -----
            url (str): The URL to be searched for.
            all_posts (bool): If True, all the contents of the URL will be returned.

        Returns:
        --------
            list: The contents of a specific URL.
        """

        return self.list_posts_from_url(self.URL("old"), all_posts)

    def publish_post(self, title, content, reference=None):
        """
        Publish a content.

        Args:
        -----
            title (str): The title of the content.
            content (str): The content.
            reference (str): The URL of the content's source.

        Returns:
        --------
            dict | object: The content's data.
        """

        data = {"title": title, "body": content, "status": "published"}

        if reference:
            if not url_validator(reference):
                raise BadUrl(
                    "A URL de referência fornecida para a postagem não é válida."
                )
            data["source_url"] = reference

        return self.post(Config.CONTENTS_URL, data)

    def delete_post(self, slug):
        """
        Delete a content.

        Args:
        -----
            slug (str): The slug of the content.

        Returns:
        --------
            dict | object: The content's data.
        """

        username = self.get_user().username
        url = Config.CONTENTS_URL + "/" + username + "/" + slug
        data = {"status": "deleted"}

        return self.patch(url, data)

    def edit_post(self, username, slug, title, content, reference=None):
        """
        Edit a content.

        Args:
        -----
            username (str): The username of the content's author.
            slug (str): The slug of the content.
            title (str): The title of the content.
            content (str): The content.
            reference (str): The URL of the content's source.

        Returns:
        --------
            dict | object: The content's data.
        """

        url = Config.CONTENTS_URL + "/" + username + "/" + slug
        data = {"title": title, "body": content, "status": "published"}

        if reference:
            if not url_validator(reference):
                raise BadUrl(
                    "A URL de referência fornecida para a edição da postagem não é válida."
                )
            data["source_url"] = reference

        return self.patch(url, data)
