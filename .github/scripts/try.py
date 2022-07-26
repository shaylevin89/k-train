import requests
import os

TOKEN = os.getenv('TOKEN')
DOCKER_REPO_NAME = os.getenv('DOCKER_REPO_NAME')
DOCKER_IMAGE_NAME = os.getenv('DOCKER_IMAGE_NAME')
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
}

url = f'https://hub.docker.com/v2/repositories/{DOCKER_REPO_NAME}/{DOCKER_IMAGE_NAME}/tags'
response = requests.get(url, headers=headers)
print(response.json())