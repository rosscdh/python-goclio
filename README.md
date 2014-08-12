python-goclio
=============

Python Client for GoClio api


```
import requests as r
response = r.get('https://app.goclio.com/api/v2/activities', headers={'Authorization': 'Bearer :token'})


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