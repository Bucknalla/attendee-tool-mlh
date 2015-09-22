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
    user_str = ''

    special_user = [item for item in user["data"]
        if item["special_needs"] != None]
    if special_user == []:
        return 'No attendees with medical needs.'
    else:
        for users in special_user:
            user_str += users['first_name'] + " " + users['last_name'] + " : " + users['special_needs'] +'\n'
        return user_str

def search_user(name):
    user = fetch_user()
    user_str = ''

    found_users = [item for item in user["data"]
        if (item["first_name"] + " " + item["last_name"]) == name or item['first_name'] == name or item['last_name'] == name]

    for user in found_users:
        user_id = "ID: " + str(user['id']) + '\n'
        first_name = "First Name: " + user['first_name'] + '\n'
        last_name = "Last Name: " + user['last_name'] + '\n'
        phone_number = "Phone Number: " + user['phone_number'] + '\n'
        email = "Email: " + user['email'] + '\n'
        gender = "Gender: " + user['gender'] + '\n'
        major = "Major: " + user['major'] + '\n'
        date_of_birth = "D.O.B: " + user['date_of_birth'] + '\n'
        school = "School: " + user['school']['name'] + '\n'
        diet = "Dietary Restrictions: " + user['dietary_restrictions'] + '\n'
        medical = "Medical Needs: " + str(user['special_needs']) + '\n'
        shirt_size = "Shirt Size: " + user['shirt_size'] + '\n'
        user_str += user_id+first_name+last_name+phone_number+email+gender+major+date_of_birth+school+diet+medical+shirt_size+'\n'
    return user_str
