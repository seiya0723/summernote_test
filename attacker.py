import requests,bs4

## wysiwyg(django-summernote)でXSSが通ってしまう問題の対処。

URL     = "http://127.0.0.1:8000/"
TIMEOUT = 10
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

client = requests.session()
client.get(URL,timeout=TIMEOUT,headers=HEADERS)

if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']

data            = { "csrfmiddlewaretoken":csrftoken }
data["comment"] = '<input type="button" onclick="alert(\'test\');">'

r   = client.post(URL,data=data,headers={"Referer":URL})
print(r)

