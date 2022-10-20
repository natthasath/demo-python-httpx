import httpx
import base64

with httpx.Client() as client:
    r = client.get('https://example.com', auth=('alice', 'ecila123'))
_, _, auth = r.request.headers['Authorization'].partition(' ')
print(auth)
print(base64.b64decode(auth))