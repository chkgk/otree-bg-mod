from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def before_next_page(self):
        print('trying background task')
        self.player.run_bg_task()


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
