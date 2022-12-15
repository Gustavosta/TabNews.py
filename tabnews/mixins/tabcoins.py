from tabnews.config import Config
from tabnews.exceptions import InsufficientTabcoins


class TabcoinsMixin:
    def upvote(self, username, slug_or_parent_id, upvote_amount=1):
        tabcoins_limit = self.get_user()['tabcoins']
        url = Config.CONTENTS_URL+'/'+username+'/'+slug_or_parent_id+'/tabcoins'
        data = {
            "transaction_type": "credit"
        }

        if upvote_amount*2 > tabcoins_limit:
            raise InsufficientTabcoins(f'Você não possui tabcoins suficientes para realizar essa ação!\nVocê possui {tabcoins_limit} tabcoins, mas precisa de {upvote_amount*2} para realizar essa ação.')
        else:
            result = {'tabcoins': None}
            for i in range(upvote_amount):
                result = self.post(url, data)

            return result

    def downvote(self, username, slug_or_parent_id, downvote_amount=1):
        tabcoins_limit = self.get_user()['tabcoins']
        url = Config.CONTENTS_URL+'/'+username+'/'+slug_or_parent_id+'/tabcoins'
        data = {
            "transaction_type": "debit"
        }

        if downvote_amount*2 > tabcoins_limit:
            raise InsufficientTabcoins(f'Você não possui tabcoins suficientes para realizar essa ação!\nVocê possui {tabcoins_limit} tabcoins, mas precisa de {downvote_amount*2} para realizar essa ação.')
        else:
            result = {'tabcoins': None}
            for i in range(downvote_amount):
                result = self.post(url, data)

            return result



