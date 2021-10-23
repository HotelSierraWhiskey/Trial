from bs4 import BeautifulSoup
import json
import os
import re


chat_html = open('application/templates/chat.html', 'r+')
chat_config_json = open('chat_config.json', 'r')
soup = BeautifulSoup(chat_html, 'html.parser')
room_names = json.load(chat_config_json)


for id, room_name in room_names['room_names'].items():
    anchor = soup.find(id=id)
    old_url = anchor['href']
    new_url = "/rooms/" + room_name
    with open('application/templates/chat.html', 'r+') as file:
        contents = file.read()
        contents = re.sub(old_url, new_url, contents)
        contents = re.sub(anchor.span.text, room_name, contents)
        file.seek(0)
        file.write(contents)
        file.truncate()

