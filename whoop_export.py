from datetime import datetime
from dotenv import load_dotenv
import requests
import os

load_dotenv()

#################################################################
# GET ACCESS TOKEN

# Post credentials
response = requests.post("https://api-7.whoop.com/oauth/token", json={
    "grant_type": "password",
    "issueRefresh": False,
    "password": os.getenv('USER_PASSWORD'),
    "username": os.getenv('USER_USERNAME')
})


# Exit if fail
if response.status_code != 200:
    print("Fail - Credentials rejected.")
    exit()
else:
    print("Success - Credentials accepted")

# Set userid/token variables
userid = response.json()['user']['id']
access_token = response.json()['access_token']

#################################################################
# GET DATA

# Download data
url = 'https://api-7.whoop.com/users/{}/cycles'.format(userid)

params = {
    'start': '2021-01-03T00:00:00.000Z',
    'end': '2021-01-03T00:00:00.000Z'
}

headers = {
    'Authorization': 'bearer {}'.format(access_token)
}

response = requests.get(url, params=params, headers=headers)

# Check if user/auth are accepted
if response.status_code != 200:
    print("Fail - User ID / auth token rejected.")
    exit()
else:
    print("Success - User ID / auth token accepted")

#################################################################
# PARSE/TRANSFORM DATA

# Convert data to json
data_raw = response.json()
print(data_raw)
