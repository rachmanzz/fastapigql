from configs.database import Model
from orator.orm import has_one, has_many
from .account import Account


class User(Model):

    @has_one
    def account(self):
        return Account

