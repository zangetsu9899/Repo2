#!/usr/bin/python3 ##shebang

# URL =: https://notes.ayushsharma.in/technology
import requests

url = 'https://notes.ayushsharma.in/technology'

data = requests.get(url)

print(data.text)