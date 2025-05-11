import requests
import json

requests.get('http://216.10.245.166/Library/GetBook.php?ID=3389')

req_json = requests.get('http://216.10.245.166/Library/GetBook.php').json()

print(req_json)

