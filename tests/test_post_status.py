
import pytest
import os
import json
from status.status_app import StatusApp

def test_status_app():
    app = StatusApp() 

    app.initialize(
            pem_file='../statusreportingapp.2021-05-29.private-key.pem',
            path_to_repo=app.generateCandidateRepoPath()
            )
    # For testing purposes we will use the first commit of the repo
    #first_commit_of_repo = 'b71e903d0c59620b15257227c8d832fa4c5f0221'

    commit_test_pending = '94eed4b8ffbfae827c42f0a8950ddb4e5c75c250'
    app.postStatus(
            'pending',
            commit_sha=first_commit_of_repo,
            context='Status App Test')
    data = app.getStatus(first_commit_of_repo)

    commit_test_error = ''
    print(json.dumps(data, indent=4))
