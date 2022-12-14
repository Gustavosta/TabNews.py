from tabnews.config import Config


class GetUserMixin:

    def get_user(self):
        url = Config.USER_DATA_URL
        response = self.get(url)
        return response.json()



