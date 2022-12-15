from tabnews.utils import url_validator
from tabnews.exceptions import BadUrl
from tabnews.config import Config


class PostMixin:
    def get_post(self, username, slug):
        url = Config.CONTENTS_URL+'/'+username+'/'+slug
        return self.get(url)


    def list_posts_from_url(self, url, all_posts=False):
        posts = []
        page = 1
        while True:
            if '?' in url:
                prefix = '&'
            else:
                prefix = '?'

            data = self.get(url+f'{prefix}page={page}')
            if not data:
                break
            posts.extend(data)
            if not all_posts:
                break
            page += 1
        return posts


    def get_posts_from_user(self, username, all_posts=False):
        url = Config.CONTENTS_URL+'/'+username
        return self.list_posts_from_url(url, all_posts)
    

    def get_relevant_posts(self, all_posts=False):
        url = Config.CONTENTS_URL+'?strategy=relevant'
        return self.list_posts_from_url(url, all_posts)	
    

    def get_new_posts(self, all_posts=False):
        url = Config.CONTENTS_URL+'?strategy=new'
        return self.list_posts_from_url(url, all_posts)
    

    def get_old_posts(self, all_posts=False):
        url = Config.CONTENTS_URL+'?strategy=old'
        return self.list_posts_from_url(url, all_posts)


    def publish_post(self, title, content, reference=None):
        data = {
            "title": title,
            'body': content,
            'status': 'published'
        }

        if reference:
            if not url_validator(reference):
                raise BadUrl('A URL de referência fornecida para a postagem não é válida.')
            data['source_url'] = reference
            
        return self.post(Config.CONTENTS_URL, data)


    def delete_post(self, username, slug):
        url = Config.CONTENTS_URL+'/'+username+'/'+slug
        data = {
            'status': 'deleted'
        }
        
        return self.patch(url, data)
    
    def edit_post(self, username, slug, title, content, reference=None):
        url = Config.CONTENTS_URL+'/'+username+'/'+slug
        data = {
            "title": title,
            'body': content,
            'status': 'published'
        }

        if reference:
            if not url_validator(reference):
                raise BadUrl('A URL de referência fornecida para a edição da postagem não é válida.')
            data['source_url'] = reference
            
        return self.patch(url, data)

    
