import re
import json
import requests
import urlparse

from requests_oauth2 import OAuth2

class Session(object):
    site = 'https://app.goclio.com/'
    authorization_url = '/oauth/authorize'
    token_url = '/oauth/token'
    response_type = 'code'
    token = None
    def __init__(self, client_id, client_secret, redirect_uri=None, **kwargs):
        self.token = None  # reset
        self.client = OAuth2(client_id=client_id,
                             client_secret=client_secret,
                             site=self.site,
                             redirect_uri=redirect_uri,
                             authorization_url=kwargs.get('authorization_url', self.authorization_url),
                             token_url=kwargs.get('token_url', self.token_url)) 
    @property
    def auth_url(self):
        return self.client.authorize_url(self.authorization_url,
                                         response_type=self.response_type)
    def token_from_code(self, code):
        self.token_response = self.client.get_token(code=code)
        self.access_token = self.token_response.get('access_token')
        return self.access_token


class BaseApi(object):
    base_url = 'https://app.goclio.com/api/v2/'
    r = requests

    def __init__(self, token, **kwargs):
        self.token = token
        self.response = self.response_json = {}
        self.params = kwargs

    @property
    def auth(self):
        return {'Authorization': 'Bearer %s' % self.token}

    @property
    def status_code(self):
        return getattr(self.response, 'status_code', None)

    @property
    def ok(self):
        return getattr(self.response, 'ok', None)

    @property
    def parse_uri(self):
        uri = self.uri

        for k, v in self.params.iteritems():
            key = ':{key}'.format(key=k)
            uri = uri.replace(key, str(v))
        
        return re.sub(r'\/\:(\w)+', '', uri)

    def headers(self, **kwargs):
        headers = {'Content-Type': 'application/json'}
        headers.update(kwargs)
        headers.update(self.auth)
        return headers

    def wrap_namespace(self, **kwargs):
        return json.dumps(kwargs)

    def endpoint(self, *args, **kwargs):
        return urlparse.urljoin(self.base_url, self.parse_uri, *args, **kwargs)

    def process(self, response):
        self.response = response
        if response.ok is True:
            self.response_json = self.response.json()
            return self.response_json
        #
        # Handle the bad CLI api implementation of 404 returning HTML and not
        # a valid REST reponse
        #
        return {'message': response.reason, 'ok': response.ok, 'status_code': response.status_code, 'url': response.url}

    def get(self, **kwargs):
        return self.process(response=self.r.get(self.endpoint(), headers=self.headers(), params=kwargs))

    def post(self, **kwargs):
        return self.process(response=self.r.post(self.endpoint(), headers=self.headers(), data=self.wrap_namespace(**kwargs)))

    def put(self, **kwargs):
        return self.process(response=self.r.put(self.endpoint(), headers=self.headers(), data=self.wrap_namespace(**kwargs)))

    def patch(self, **kwargs):
        return self.process(response=self.r.patch(self.endpoint(), headers=self.headers(), data=self.wrap_namespace(**kwargs)))

    def delete(self, **kwargs):
        return self.process(response=self.r.delete(self.endpoint(), headers=self.headers(), params=kwargs))


class Me(BaseApi):
    uri = 'users/who_am_i'


class Matters(BaseApi):
    uri = 'matters/:id'

    def wrap_namespace(self, **kwargs):
        return super(Matters, self).wrap_namespace(matter=kwargs)


class Documents(BaseApi):
    uri = 'documents/:id'

    def wrap_namespace(self, **kwargs):
        return {'document': kwargs}

    def document_versions(self):
        return self.response_json.get('document', {}).get('document_versions', self.get().get('document', {}).get('document_versions',[]))

    def download_version(self, version_id):
        download = self.DownloadVersion(token=self.token, id=self.response_json.get('document', {}).get('id'), document_version=version_id)
        return download.get()

    class DownloadVersion(BaseApi):
        uri = 'documents/:id/document_version/:document_version/download'


class DocumentCategories(BaseApi):
    uri = 'document_categories'

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
