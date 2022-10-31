# Related third party imports
from flask import (
    jsonify,
    request,
    send_file,
)

from app.showcase.models import (
    User,
    Repository,
)

from app.utils.chart import (
    Chart
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
            maxContributors = request.args.get('limit', type=int, default=5)
            contributors_list = Repository.get_contributors_list(owner, repository, maxContributors)
            if(contributors_list==False):
                return "Some error occured", 400
            else:
                response={}
                response["repository"]=repository
                response["owner"]=owner
                response["contributors_count"]=len(contributors_list)
                response["contributors"]=contributors_list
                Chart.generate_chart(response)
                return send_file('./../static/images/bar_chart.svg', mimetype='image/svg+xml'), 200

                
        