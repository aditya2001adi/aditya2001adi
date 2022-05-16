from http import cookies
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

s = requests.session()

nyt_login_url = 'https://myaccount.nytimes.com/'

login_route = 'svc/lire_ui/login'

csrf_token = 'H4sIAAAAAAAAA32QS2vDMBCE/4sgPZnYUiz5AaH00IDTUx+B3Iwe60REtoUkJw1p/nsVH3so7GWGnY/ZvSGptUI16iZjWssPgBIkjYYhzPZZR620t4ZfUd1x4yFB8G21A49qzCguWYVzliB7ngMKE5rhKsskBQ5EECpzLgsghOS8LFnEOeAKXPPYnpWKMBnayenoHEOwvk7Ty+WyHK5B9+CXcuxTPwkvnbZBj0PaTyZo60Y1yZAaW7697z6Xx9CbZ8l7y/VhaNS62G62+6fXffPV7j6a9QxerF4WZBPnDz46cxVvx8FDG64WYhc5jif9eEhwJ1TfEPceQvR77sMxHjFHOnAOXGxv/mmP7vcfShgjTFEhMlVQhpkqyqrDKl/lVMgu76gigouuwkUcJnBFBSdMUslKWuX8F+/ahtKrAQAA'

HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
   'origin': nyt_login_url,
   'referer': nyt_login_url + login_route
}

login_payload = {
    'login': 'abab2019@mymail.pomona.edu',
    'password': 'Adi23adi!',
    'csrftoken': csrf_token
}

login_req = s.post(nyt_login_url + login_route, headers = HEADERS, data = login_payload)

print(login_req.raise_for_status())


