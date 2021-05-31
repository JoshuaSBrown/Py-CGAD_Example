
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
            commit_sha=commit_test_pending,
            context='Status App Test')

    commit_test_error = '2c7d52e095be03b896f380b86bd036990d6ffcc8'
    app.postStatus(
            'error',
            commit_sha=commit_test_error,
            context='Status App Test')

    commit_test_success = '9f5c45fd76e1b17e1076d7226642e819e4b59aa1'
    app.postStatus(
            'success',
            commit_sha=commit_test_success,
            context='Status App Test')

    data = app.getStatus(first_commit_of_repo)
    print(json.dumps(data, indent=4))
