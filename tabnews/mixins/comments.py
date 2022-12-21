#!/usr/bin/python
# -*- coding: utf-8 -*-

from tabnews.config import Config


class CommentMixin:
    def get_comments(self, username, slug):
        """
        Get the comments of a specific content.
        
        Args:
        -----
            username (str): The username of the content's author.
            slug (str): The slug of the content.
            
        Returns:
        --------
            list: The comments of a specific content.
        """
        
        url = Config.CONTENTS_URL+'/'+username+'/'+slug+'/'+'children'
        return self.get(url)


    def publish_comment(self, parent_id, content):
        """
        Publish a comment.
        
        Args:
        -----
            parent_id (str): The id of the content to which the comment will be published.
            content (str): The content of the comment.
        
        Returns:
        --------
            dict | object: The comment's data.
        """
        
        data = {
            'parent_id': parent_id,
            'body': content,
            'status': 'published'
        }

        return self.post(Config.CONTENTS_URL, data)


    def delete_comment(self, comment_slug):
        """
        Delete a comment.
        
        Args:
        -----
            comment_slug (str): The slug of the comment.
        
        Returns:
        --------
            dict | object: The comment's data.
        """
        
        username = self.get_user()['username']
        url = Config.CONTENTS_URL+'/'+username+'/'+comment_slug
        data = {
            'status': 'deleted'
        }
        
        return self.patch(url, data)
    

    def edit_comment(self, comment_slug, parent_id, content):
        """
        Edit a comment.
        
        Args:
        -----
            comment_slug (str): The slug of the comment.
            parent_id (str): The id of the content to which the comment will be published.
            content (str): The content of the comment.
        
        Returns:
        --------
            dict | object: The comment's data.
        """
        
        username = self.get_user()['username']
        url = Config.CONTENTS_URL+'/'+username+'/'+comment_slug
        data = {
            'parent_id': parent_id,
            'body': content,
            'status': 'published'
        }
        
        self.patch(url, data)
