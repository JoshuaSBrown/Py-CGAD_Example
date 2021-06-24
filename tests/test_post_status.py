import pytest
import os
import json
from status.status_app import StatusApp


@pytest.fixture
def test_app():
    app = StatusApp()

    current_path, _ = os.path.split(os.path.abspath(__file__))
    repo_path = os.path.normpath(os.path.join(current_path, "../"))
    for file_name in os.listdir(repo_path):
        if file_name.lower().endswith(".pem"):
            if "statusreportingapp" in file_name:
                print("Found pem file {}".format(file_name))
                pem_file_path = os.path.join(repo_path, file_name)
                break

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

    # This is because of the ci we are testing different python version in
    # parallel and we don't want to overwrite changes to the status
    commit_for_python_version3_7 = "5ac6e084ccdfd9375537a485345f2909b748648e"
    commit_for_python_version3_8 = "a76b68983e42255589cda8b4de47133aef22c984"
    commit_for_python_version3_9 = "7aa7fdc0871c6d8484f47050f6e839e9b7ee4691"

    test_commit = commit_for_python_version3_7
    if sys.version_info[0] == 3:
        if sys.version_info[1] == 8:
            test_commit = commit_for_python_version3_8
        elif sys.version_info[1] == 9:
            test_commit = commit_for_python_version3_9

    test_app.postStatus("pending", commit_sha=test_commit)
    # Will return the latest state which should now be pending
    state, code, _ = test_app.getState(test_commit)
    assert state == "pending"
    assert code == 200
    test_app.postStatus("success", commit_sha=test_commit)
    state, code, _ = test_app.getState(test_commit)
    assert state == "success"
    assert code == 200
