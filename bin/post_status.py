import argparse
from status.status_app import StatusApp


def main(**kwargs):

    app = StatusApp(kwargs["verbose"])
    app.initialize(pem_file=kwargs["permissions"])
    app.postStatus(kwargs["status"], context="Status App")
    app.printStatus()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        "Example implementation of Py-CGAD, will post generic message to provided commit hash"
    )

    desc = "What is the state of the status: success, failed, error, pending"

    parser.add_argument("--status", "-s", type=str, nargs=1, required=True, help=desc)

    desc = "Permissions file, allows us to interact with the github repository"

    parser.add_argument(
        "--permissions", "-p", type=str, nargs=1, required=True, help=desc
    )

    desc = "Vebosity of output."

    parser.add_argument("--verbose", "-v", type=int, nargs=1, default=0, help=desc)

    args = parser.parse_args()

    main(**vars(args))
