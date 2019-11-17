#!/usr/bin/env python3

from datetime import date
from os import environ
import requests

date_str = str(date.today())
release_request = {
    "tag_name": date_str,
    "target_commitish": "master",
    "name": date_str,
    "body": f"Updated on {date_str}"
}

repo = environ.get("GITHUB_REPOSITORY")
url = f"https://api.github.com/repos/{repo}/releases"

token = environ.get("GITHUB_TOKEN")
assert token, "GITHUB_TOKEN not found"
headers = {
    "Authorization": f"Bearer {token}"
}
print(url)
print(release_request)
resp = requests.post(url, json=release_request, headers=headers)
print(resp)
resp.raise_for_status()
