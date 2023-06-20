from requests import Session
from allure import step
import logging
import curlify
import allure
from allure_commons.types import AttachmentType


class BaseSession(Session):

    def __init__(self, **kwargs):
        super().__init__()
        self.base_url_api = kwargs.pop('base_url')
        self.params = {}
        self.json = None

    def request(self, method, url, **kwargs):
        with step(f'{method} {url}'):
            response = super().request(method, url=f'{self.base_url_api}{url}', **kwargs)
            content_type = response.headers['content-type']
            logging.info(curlify.to_curl(response.request))
            if 'text' in content_type:
                logging.info(response.text)
            elif 'json' in content_type:
                logging.info(response.json())
            log = str(response.json())
            allure.attach(f'status_code: {response.status_code} {curlify.to_curl(response.request)}', 'request',
                          AttachmentType.TEXT, '.log')
            allure.attach(log, 'response', AttachmentType.TEXT, '.log')

            return response

    def post(self, url, data=None, json=None, **kwargs):
        return super().post(url, json=self.json, **kwargs)

    def get(self, url, entity='', **kwargs):
        return super().get(url=f"{url}{entity}", **kwargs)

    def delete(self, url, entity='', **kwargs):
        return super().delete(url=f"{url}{entity}", **kwargs)
