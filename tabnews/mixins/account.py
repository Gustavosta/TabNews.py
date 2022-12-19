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
            response = self.get(url)
            return response
        
        else:
            url = Config.USERS_DATA_URL+f'/{username}'
            response = self.get(url)
            response = response

            # These additional fields serve to match the fields of searching 
            # for a user with that of searching for the user himself, since 
            # they have different returns for security reasons
            response['email'] = None
            response['notifications'] = None

            return response
