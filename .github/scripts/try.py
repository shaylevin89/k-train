import requests
import os
from datetime import datetime

DOCKER_REPO_NAME = os.getenv('DOCKER_REPO_NAME')
DOCKER_IMAGE_NAME = os.getenv('DOCKER_IMAGE_NAME')
DOCKERHUB_USER = os.getenv('DOCKERHUB_USER')
DOCKERHUB_PASSWD = os.getenv('DOCKERHUB_PASSWD')

data = {"username": DOCKERHUB_USER, "password": DOCKERHUB_PASSWD}


url = "https://hub.docker.com/v2/users/login/"
response2 = requests.post(url, data=data)
TOKEN = response2.json()['token']
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
}

url = f'https://hub.docker.com/v2/repositories/{DOCKER_REPO_NAME}/{DOCKER_IMAGE_NAME}/tags'
response = requests.get(url, headers=headers)
j_res = response.json()

latest_update = ''
last_version = ''
for image_info in j_res['results']:
    if image_info['name'] != 'latest':
        last_time = datetime.strptime(image_info['last_updated'], "%Y-%m-%dT%H:%M:%S.%fZ")
        if not latest_update or last_time > latest_update:
            latest_update = last_time
            last_version = image_info['name']

print(last_version)
print(latest_update)

SEMVER_LEVEL = os.getenv('SEMVER_LEVEL')

if SEMVER_LEVEL == 'major':
    new_version = f"v{int(last_version.split('.')[0][1:]) + 1}.0.0"
elif SEMVER_LEVEL == 'minor':
    new_version = f"{last_version.split('.')[0]}.{int(last_version.split('.')[1]) + 1}.0"
else:
    new_version = f"{last_version.split('.')[0]}.{last_version.split('.')[1]}.{int(last_version.split('.')[2]) + 1}"
print(f"last: {last_version} new: {new_version}")

os.system(f'echo "DOCKER_TAG={new_version}" >> $GITHUB_ENV')