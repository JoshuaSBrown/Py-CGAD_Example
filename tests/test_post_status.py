
import pytest
import os
import json
from status.status_app import StatusApp

@pytest.fixture
def test_app():
    app = StatusApp() 

    app.initialize(
            pem_file='../statusreportingapp.2021-05-29.private-key.pem',
            path_to_repo=app.generateCandidateRepoPath()
            )

    return app


def test_get_status(test_app):

    commit_test_pending = '94eed4b8ffbfae827c42f0a8950ddb4e5c75c250'
    # Should only be a single status for this commit 
    data_pending, code = test_app.getStatuses(commit_test_pending)
    print(json.dumps(data_pending, indent=4))
    print(code)
    assert len(data_pending) == 1
    assert data_pending[0]['state'] == 'pending'
    assert code == 200

    commit_test_error = '2c7d52e095be03b896f380b86bd036990d6ffcc8'
    # Should only be a single status for this commit 
    data_error, code = test_app.getStatuses(commit_test_error)
    print(json.dumps(data_error, indent=4))
    print(code)
    assert len(data_error) == 1
    assert data_error[0]['state'] == 'error'
    assert code == 200

    commit_test_success = '9f5c45fd76e1b17e1076d7226642e819e4b59aa1'
    # Should only be a single status for this commit 
    data_success, code = test_app.getStatuses(commit_test_success)
    print(json.dumps(data_success, indent=4))
    print(code)
    assert len(data_success) == 1
    assert data_success[0]['state'] == 'success'
    assert code == 200

def test_post_status(test_app):
    # For testing purposes we will use the first commit of the repo
    #first_commit_of_repo = 'b71e903d0c59620b15257227c8d832fa4c5f0221'
    #data = app.getStatus(first_commit_of_repo)
    #print(json.dumps(data, indent=4))
