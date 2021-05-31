
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

    commit_test_pending = '5788421d9a356e4705b83e4ff3b8472f8ff86589'
    app.postStatus(
            'pending',
            commit_sha=first_commit_of_repo,
            context='Status App Test')
    data = app.getStatus(first_commit_of_repo)
    print(json.dumps(data, indent=4))
