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
