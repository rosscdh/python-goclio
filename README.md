python-goclio
=============

(in-development) Python Client for GoClio api

Please use in conjunction with https://github.com/rosscdh/python-social-auth.git@backends/goclio (oauth2 implementation for goclio; has a pull request pending on the primary project).

This will then provide you with access to the ":token" which is the oauth2 token mentioned in the examples below.

```
#
# Create an OAuth2 Session token
#
from goclio.clio import Session

CLIENT_KEY = ':your_client_id'
CLIENT_SECRET = ':your_client_secret'

s = Session(client_id=CLIENT_KEY,
            client_secret=CLIENT_SECRET)

print s.auth_url
>>> 'https://app.goclio.com//oauth/authorize?scope=%2Foauth%2Fauthorize&redirect_uri=None&response_type=code&client_id=:your_client_id'

token = s.token_from_code(code='xrwrfDHdHtOYLs2NZejJ')

#
# Use the token provided above to use the api in the following manner
#


from goclio.clio import Me
s=Me(token=':token')
s.get()


from goclio.clio import Matters
s=Matters(token=':token')
s.get()


from goclio.clio import Matters
m=Matters(token=':token')
m.post(client_id=882801947, description='a test matter', status='Open')


from goclio.clio import Matters
m=Matters(token=':token', id=1025003373)
m.get()


from goclio.clio import Documents
s=Documents(token=':token')
s.get()


from goclio.clio import Documents
d=Documents(token=':token', id=28745759)
d.document_versions()
d.download_version(version_id=30613503)

d.get()
v=d.version(version_id=30613503)

from goclio.clio import DocumentCategories
s=DocumentCategories(token=':token')
s.get()
```

To paginate and basically do anythign via GET params (as per goclio api docs) pass in the desired param arguments as keyword arguments i.e. "s.get(offset=2)".


ToDo
----

1. Self contained session to provideo oauth2 token
2. Examples of pagination and other api operators
3. Tests
4. Better docs
