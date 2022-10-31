# Related third party imports
import json
import requests


class User:

    def check_owner_validity(username):
        github_response = requests.get('https://api.github.com/users/'+username)
        if github_response.status_code==200:
            return True
        else:
            False


class Repository:

    def check_repository_status(owner, repository):
        github_response = requests.get('https://api.github.com/repos/'+owner+'/'+repository)
        if github_response.status_code==200:
            return True
        else:
            False

    def get_contributors_list(owner, repository):
        github_response = requests.get('https://api.github.com/repos/'+owner+'/'+repository+'/contributors')
        if github_response.status_code==200:
            return github_response.json()
        else:
            return False

