import requests
import urlparse


class BaseApi(object):
    base_url = 'https://app.goclio.com/api/v2/'
    r = requests

    def __init__(self, token, **kwargs):
        self.token = token
        self.response = self.response_json = {}

    @property
    def auth(self):
        return {'Authorization': 'Bearer %s' % self.token}

    @property
    def status_code(self):
        return getattr(self.response, 'status_code', None)

    @property
    def ok(self):
        return getattr(self.response, 'ok', None)

    def endpoint(self, *args, **kwargs):
        return urlparse.urljoin(self.base_url, self.uri, *args, **kwargs)

    def process(self, response):
        self.response = response
        self.response_json = self.response.json()
        return self.response_json

    def get(self, **kwargs):
        return self.process(response=self.r.get(self.endpoint(), headers=self.auth, **kwargs))

    def post(self, **kwargs):
        return self.process(response=self.r.get(self.endpoint(), headers=self.auth, **kwargs))

    def put(self, **kwargs):
        return self.process(response=self.r.get(self.endpoint(), headers=self.auth, **kwargs))

    def patch(self, **kwargs):
        return self.process(response=self.r.get(self.endpoint(), headers=self.auth, **kwargs))

    def delete(self, **kwargs):
        return self.process(response=self.r.get(self.endpoint(), headers=self.auth, **kwargs))


class Me(BaseApi):
    uri = 'users/who_am_i'


class Matters(BaseApi):
    uri = 'matters'


class Documents(BaseApi):
    uri = 'documents'

    class Categories(BaseApi):
        uri = 'document_categories'

    class Versions(BaseApi):
        uri = 'documents/:document_id/document_version/:id/download'


# class Notes(BaseApi):
#     uri = 'notes'


# class Contacts(BaseApi):
#     uri = 'contacts'


# class Activities(BaseApi):
#     uri = 'activities'

#     class Descriptions(BaseApi):
#         uri = 'activity_descriptions'


# class Bills(BaseApi):
#     uri = 'bills'


# class Calendars(BaseApi):
#     uri = 'calendars'

#     class Entries(BaseApi):
#         uri = 'calendar_entries'
