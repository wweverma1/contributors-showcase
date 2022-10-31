# Related third party imports
import json
import requests

from app import (
    GITHUB_TOKEN,
)

class User:

    def check_owner_validity(username):
        header = {"Authorization": "Bearer "+GITHUB_TOKEN}
        github_response = requests.get('https://api.github.com/users/'+username, headers=header)
        print(github_response)
        if github_response.status_code==200:
            return True
        else:
            False


class Repository:

    def check_repository_status(owner, repository):
        header = {"Authorization": "Bearer "+GITHUB_TOKEN}
        github_response = requests.get('https://api.github.com/repos/'+owner+'/'+repository, headers=header)
        if github_response.status_code==200:
            return True
        else:
            False

    def get_contributors_list(owner, repository, maxContributors):
        header = {"Authorization": "Bearer "+GITHUB_TOKEN}
        github_response = requests.get('https://api.github.com/repos/'+owner+'/'+repository+'/contributors?per_page='+str(maxContributors), headers=header)
        if github_response.status_code==200:
            return github_response.json()
        else:
            return False

