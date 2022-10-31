# Related third party imports
from flask import (
    jsonify,
    request,
)

from app.showcase.models import (
    User,
    Repository,
)


def generate_contributors_showcase():
    owner = request.args.get('owner', type=str)
    if(not User.check_owner_validity(owner)):
        return "Owner doesn't exists", 400
    else:
        repository = request.args.get('repository', type=str)
        if(not Repository.check_repository_status(owner, repository)):
            return "Private Reposiotry/ Repository doesn't exists", 400
        else:
            contributors_list = Repository.get_contributors_list(owner, repository)
            if(contributors_list==False):
                return "Some error occured", 400
            else:
                response={}
                response["repository"]=repository
                response["owner"]=owner
                response["contributors_count"]=len(contributors_list)
                response["contributors"]=contributors_list
                return jsonify(response), 200

                
        