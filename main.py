import httpx

class Method:
    def get():
        r = httpx.get(f"https://httpbin.org/get")
        return r.text

    def put():
        r = httpx.put(f"https://httpbin.org/put", data={'key': 'value'})
        return r.text

    def delete():
        r = httpx.delete(f"https://httpbin.org/delete")
        return r.text

    def head():
        r = httpx.head(f"https://httpbin.org/get")
        return r.text

    def options():
        r = httpx.options(f"https://httpbin.org/get")
        return r.text

    def params():
        params = {'key1': 'value1', 'key2': 'value2'}
        r = httpx.get(f"https://httpbin.org/get", params=params)
        return r.text

    def params_list():
        params = {'key1': 'value1', 'key2': ['value2', 'value3']}
        r = httpx.get(f"https://httpbin.org/get", params=params)
        return r.text

    def content_text():
        r = httpx.get('https://www.example.org/')
        return r.text

    def content_binary():
        r = httpx.get('https://www.example.org/')
        return r.content

    def content_json():
        r = httpx.get('https://api.github.com/events')
        return r.json()

    def headers_custom():
        url = 'https://httpbin.org/headers'
        headers = {'user-agent': 'my-app/0.0.1'}
        r = httpx.get(url, headers=headers)
        return r.text

    def post_data():
        r = httpx.post(f"https://httpbin.org/post", data={'key': 'value'})
        return r.text

    def post_json():
        data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
        r = httpx.post("https://httpbin.org/post", json=data)
        return r.text

    def post_binary():
        content = b'Hello, world'
        r = httpx.post("https://httpbin.org/post", content=content)
        return r.text

    def post_file():
        data = {'message': 'Hello, world!'}
        files = {'upload-file': open('image.jpg', 'rb')}
        r = httpx.post("https://httpbin.org/post", data=data, files=files)
        return r.text

    def post_file_custom():
        files = {'upload-file': ('report.xlsx', open('report.xlsx', 'rb'), 'application/vnd.ms-excel')}
        r = httpx.post("https://httpbin.org/post", files=files)
        return r.text

    def cookies_get():
        cookies = {"peanut": "butter"}
        r = httpx.get('https://httpbin.org/cookies', cookies=cookies)
        return r.json()

    def cookies_set():
        cookies = httpx.Cookies()
        cookies.set('cookie_on_domain', 'hello, there!', domain='httpbin.org')
        cookies.set('cookie_off_domain', 'nope.', domain='example.org')
        r = httpx.get('http://httpbin.org/cookies', cookies=cookies)
        return r.json()

    def redirection():
        r = httpx.get('http://github.com/', follow_redirects=True)
        return r.history

    def timeouts():
        r = httpx.get('https://github.com/', timeout=0.001)
        # r = httpx.get('https://github.com/', timeout=None)
        return r.status_code

    def authentication():
        auth = httpx.DigestAuth("my_user", "password123")
        r = httpx.get("https://example.com", auth=auth)
        return r.status_code

print(Method.authentication())