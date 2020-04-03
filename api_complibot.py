import json
import requests
import configparser as cfg

# create config.cfg file with bot token name under [creds]

def read_token_from_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get('creds','token')

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

# returns the new url
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

# get data from webpage
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset + 1)
    js = get_json_from_url(url)
    return js

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


token = read_token_from_file("config.cfg")  # token is stored in config.cfg under [creds]
URL = "https://api.telegram.org/bot{}/".format(token)
