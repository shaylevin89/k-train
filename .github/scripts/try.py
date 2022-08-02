import requests
import os

DOCKER_REPO_NAME = os.getenv('DOCKER_REPO_NAME')
DOCKER_IMAGE_NAME = os.getenv('DOCKER_IMAGE_NAME')
DOCKERHUB_USER = os.getenv('DOCKERHUB_USER')
DOCKERHUB_PASSWD = os.getenv('DOCKERHUB_PASSWD')

data = {"username": DOCKERHUB_USER, "password": DOCKERHUB_PASSWD}


print(f"{DOCKERHUB_USER} {DOCKERHUB_PASSWD}")
url = "https://hub.docker.com/v2/users/login/"
response2 = requests.post(url, data=data)
print(response2.json()['token'])
TOKEN = response2.json()['token']
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
}

url = f'https://hub.docker.com/v2/repositories/{DOCKER_REPO_NAME}/{DOCKER_IMAGE_NAME}/tags'
response = requests.get(url, headers=headers)
print(response.json())