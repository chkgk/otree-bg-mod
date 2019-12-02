from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'bgtask'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        print('start randomizer ')
        async_to_sync(channel_layer.send)(
            "backgroundworker",
            {
                "type": "random_values"
            },
        )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
