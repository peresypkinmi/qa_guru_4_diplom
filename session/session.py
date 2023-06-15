from requests import Session


class BaseSession(Session):

    def __init__(self, **kwargs):
        self.ui_url = kwargs.pop('base')

    pass
