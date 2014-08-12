python-goclio
=============

Python Client for GoClio api


```
from goclio.clio import Me
s=Me(token=':your_token')
s.get()


from goclio.clio import Matters
s=Matters(token=':your_token')
s.get()


from goclio.clio import Documents
s=Documents(token=':your_token')
s.get()
```