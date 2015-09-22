import requests
from flask import jsonify
import json

json_key = json.load(open('credentials.json'))

client_id = json_key['client_id']
client_secret = json_key['client_secret']


def fetch_user():
    return requests.get('https://my.mlh.io/api/v1/users?client_id=' + client_id + '&secret=' + client_secret).json()

def get_dietary_users():
    user = fetch_user()
    user_str = ''

    dietary_user = [item for item in user["data"]
        if item["dietary_restrictions"] != "None"]
    if dietary_user == []:
        return 'No attendees with dietary restrictions.'
    else:
        for users in dietary_user:
            user_str += users['first_name'] + " " + users['last_name'] + " : " + users['dietary_restrictions'] +'\n'
        return user_str

def get_special_users():
    user = fetch_user()

    special_user = [item for item in user["data"]
        if item["special_needs"] != None]
    if special_user == []:
        return 'No attendees with medical needs.'
    else:
        for users in special_user:
            user_str += users['first_name'] + " " + users['last_name'] + " : " + users['special_needs'] +'\n'
        return user_str
