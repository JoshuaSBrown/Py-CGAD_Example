import pytest
import os
import json
from status.status_app import StatusApp


@pytest.fixture
def test_app():
    app = StatusApp()

    current_path = os.path.abspath(__file__)
    repo_path = os.path.join(current_path, "../")
    repo_path = os.path.abspath(repo_path)
    pem_file_path = os.path.join(
        repo_path, "statusreportingapp.2021-05-29.private-key.pem"
    )
    app.initialize(pem_file=pem_file_path, path_to_repo=app.generateCandidateRepoPath())

    return app


def test_get_status(test_app):

    commit_test_pending = "94eed4b8ffbfae827c42f0a8950ddb4e5c75c250"
    # Should only be a single status for this commit
    data_pending, code, _ = test_app.getStatuses(commit_test_pending)
    print(json.dumps(data_pending, indent=4))
    print(code)
    assert len(data_pending) == 1
    assert data_pending[0]["state"] == "pending"
    assert data_pending[0]["context"] == "Status App Test"
    assert code == 200
    state, code, _ = test_app.getState(commit_test_pending)
    assert state == "pending"
    assert code == 200

    commit_test_error = "2c7d52e095be03b896f380b86bd036990d6ffcc8"
    # Should only be a single status for this commit
    data_error, code, _ = test_app.getStatuses(commit_test_error)
    print(json.dumps(data_error, indent=4))
    print(code)
    assert len(data_error) == 1
    assert data_error[0]["state"] == "error"
    assert data_error[0]["context"] == "Status App Test"
    assert code == 200
    state, code, _ = test_app.getState(commit_test_error)
    assert state == "error"
    assert code == 200

    commit_test_success = "9f5c45fd76e1b17e1076d7226642e819e4b59aa1"
    # Should only be a single status for this commit
    data_success, code, _ = test_app.getStatuses(commit_test_success)
    print(json.dumps(data_success, indent=4))
    print(code)
    assert len(data_success) == 1
    assert data_success[0]["state"] == "success"
    assert data_success[0]["context"] == "Status App Test"
    assert code == 200
    state, code, _ = test_app.getState(commit_test_success)
    assert state == "success"
    assert code == 200


def test_post_status(test_app):

    test_commit = "5ac6e084ccdfd9375537a485345f2909b748648e"
    test_app.postStatus("pending", commit_sha=test_commit)
    # Will return the latest state which should now be pending
    state, code, _ = test_app.getState(test_commit)
    assert state == "pending"
    assert code == 200
    test_app.postStatus("success", commit_sha=test_commit)
    state, code, _ = test_app.getState(test_commit)
    assert state == "success"
    assert code == 200
