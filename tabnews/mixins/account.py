from tabnews.config import Config


class GetUserMixin:
    def get_user(self, username=None):
        if username is None:
            url = Config.USER_DATA_URL
            response = self.get(url)
            return response.json()
        
        else:
            url = Config.USERS_DATA_URL+f'/{username}'
            response = self.get(url)
            response = response.json()

            # These additional fields serve to match the fields of searching 
            # for a user with that of searching for the user himself, since 
            # they have different returns for security reasons
            response['email'] = None
            response['notifications'] = None

            return response


