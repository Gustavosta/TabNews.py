from tabnews.utils import url_validator
from tabnews.exceptions import BadUrl
from tabnews.config import Config


class CommentMixin:
    def get_comments(self, username, slug):
        url = Config.CONTENTS_URL+'/'+username+'/'+slug+'/'+'children'
        return self.get(url)


    def publish_comment(self, parent_id, content):
        data = {
            'parent_id': parent_id,
            'body': content,
            'status': 'published'
        }

        return self.post(Config.CONTENTS_URL, data)


    def delete_comment(self, comment_slug):
        username = self.get_user()['username']
        url = Config.CONTENTS_URL+'/'+username+'/'+comment_slug
        data = {
            'status': 'deleted'
        }
        print(url)
        
        return self.patch(url, data)
    

    def edit_comment(self, comment_slug, parent_id, content):
        username = self.get_user()['username']
        url = Config.CONTENTS_URL+'/'+username+'/'+comment_slug
        data = {
            'parent_id': parent_id,
            'body': content,
            'status': 'published'
        }
        print(url)
        
        self.patch(url, data)


